# -*- coding: utf-8 -*-

from odoo import models,Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold_btn(self):
        print("============")
        print(self.buyer_id)
        estate_invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
            'invoice_line_ids': [Command.create({
                'name': self.name,
                'price_unit': self.selling_price * 0.06
            }),
            Command.create({
                'name': "Administrative Fees",
                'price_unit': 100
            })
            
            ]
        })
        
        
        return super().action_sold_btn()
