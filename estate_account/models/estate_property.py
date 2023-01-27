# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo import Command
from odoo.exceptions import ValidationError, UserError


class EstateProperty(models.Model):
    _inherit = "estate.property"

    name = fields.Char()

    def action_sold(self):
        # domain = [('state', '=', 'maintenance')]
        for record in self:
            self.env['account.move'].create(
                {
                    "partner_id": record.buyer_id.id,
                    "move_type": 'out_invoice',
                    "invoice_line_ids": [
                        (
                            0,
                            0,
                            {
                                "name": record.name,
                                "quantity": 1.0,
                                "price_unit": record.selling_price * 6.0 / 100,
                            },

                        ),
                        (
                            0,
                            0,
                            {
                                "name": "Administrative Fees",
                                "quantity": 1.0,
                                "price_unit": 100,
                            },
                        ),
                    ],
                    "line_ids": [
                        Command.create({
                            "name": record.name,
                            # "product_id": record.property_type_id.id,
                        })
                    ],
                }
            )

            self.env['project.task'].create(
                {
                    'display_name': record.name,
                    'project_id': 11,

                },
            )

        return super(EstateProperty, self).action_sold()

    # def action_sold(self):
    #     # result = super.action_sold()
    #     if self.state == 'sold':
    #         self.env.ref('account_accountant.account.move').trigger()
    #         raise UserError("nothing workung ")
    #     return result
    #     CREATE= 0
    # UPDATE= 1
    # DELETE= 2
    # UNLINK= 3
    # LINK= 4
    # CLEAR= 5
    # SET= 6
