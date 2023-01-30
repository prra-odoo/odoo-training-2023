# -*- coding: utf-8 -*-

from odoo import models, fields, Command

class EstateAccount(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        self.env["account.move"].sudo().create(
            {
                'partner_id': self.buyers_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                Command.create(
                    {
                        "name": self.name,
                        "quantity": 1,
                        "price_unit": 0.94*self.selling_price,
                    }),
                Command.create(
                    {
                        "name": "administrative fees",
                        "quantity": 1,
                        "price_unit": 100.00,
                    }
                )
            ],
            }
        )
        return super(EstateAccount,self).action_sold()