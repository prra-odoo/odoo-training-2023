# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models

class RealEstateProperty(models.Model):
    _inherit =  "real.estate.property"
    
    def action_sold_porperty(self):
        print(self)
        res = super().action_sold_porperty()
        for prop in self:
            print(prop.buyer_id.id)
            print(self.buyer_id.id)
            print(self.name)
            print(prop.name)
            self.buyer_id.id
            self.env["account.move"].sudo().create(
                {
                    "partner_id": self.buyer_id.id,
                    "move_type": "out_invoice",
                    "invoice_line_ids": [
                        (0,0,{
                                "name": self.name,
                                "quantity": 1.0,
                                "price_unit": self.selling_price
                            },),
                        (0,0,{
                                "name": "Administrative fees",
                                "quantity": 1.0,
                                "price_unit": 100.0,
                            },
                        ),],
                }
            )
        print(res)
        return res
