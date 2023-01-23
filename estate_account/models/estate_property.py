# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models

class RealEstateProperty(models.Model):
    _inherit =  "real.estate.property"
    
    def action_sold_porperty(self):
        print(self)
        res = super().action_sold_porperty()
        for prop in self:
            self.env["account.move"].create(
                {
                    "partner_id": prop.buyer_id.id,
                    "move_type": "out_invoice",
                }
            )
        print(res)
        return res
