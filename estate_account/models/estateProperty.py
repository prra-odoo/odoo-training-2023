# -- coding: utf-8 --
from odoo import fields,models,api,Command

class estateProperty(models.Model):
    _name = "estate.property"
    _inherit= "estate.property"


    def sell_property(self):
        print("override........")

        invoice = self.env['account.move'].create({
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


        
        return super().sell_property()
