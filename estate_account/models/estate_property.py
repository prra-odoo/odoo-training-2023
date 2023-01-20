# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo import Command
from odoo.exceptions import ValidationError, UserError


class EstateProperty(models.Model):
    _inherit = "estate.property"

    name = fields.Char()

    def action_sold(self):
        for record in self:
            self.env['account.move'].create(
                {
                    "partner_id": record.buyer_id.id,
                    "move_type": 'out_invoice',
                    # "invoice_line_ids": [
                    #     (
                    #         0,
                    #         0,
                    #         {
                    #             "name": record.name,
                    #             "quantity": 1.0,
                    #             "price_unit": record.selling_price.id * 6.0 / 100,
                    #         },

                    #     ),
                    # ],
                    "line_ids": [
                        Command.create({
                            "name": record.name,
                            # "product_id": record.property_type_id.id,
                        })
                    ],
                }
            )
        return super(EstateProperty, self).action_sold()
    # def action_sold(self):
    #     # res = super.action_sold()
    #     if self.state == 'sold':
    #         self.env.ref('account_accountant.account.move').trigger()
    #         raise UserError("nothing workung ")
    #     return True
