# -*- coding: utf-8 -*-

from odoo import models, fields

class EstatePropertyAccount(models.Model):
    _inherit = "estate.property"
    
    test = fields.Char(string="Testing", help="This field is for purpose.")
    
    def action_sold_btn(self):
        print(self.env)
        estate_invoice = self.env['account.move'].create([
            {
                'move_type': 'out_invoice',
                'partner_id': self.buyer_id.id,
                'invoice_line_ids': [
                    (0, 0, {                            # TODO : What is [(0, 0, {})].
                    # 'product_id': self.id,            # TODO : Remove Product field from Invoice.
                    'name': self.name,
                    'price_unit': self.selling_price,
                    'quantity': 1,
                    # 'new_price_unit': self.selling_price * 0.06,
                    })
                ],
            }
        ])
        estate_invoice.action_post()
        return super().action_sold_btn()