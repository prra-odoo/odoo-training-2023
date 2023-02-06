# # -*- coding: utf-8 -*-

from odoo import models,Command;

class inheritedEstate(models.Model):
    _inherit = "estate.property"

    def action_to_sold(self):
        res = super(inheritedEstate,self).action_to_sold()
        self.env['account.move'].check_access_rights('read')
        self.env['account.move'].check_access_rule('read')
        self.env['account.move'].sudo().create({
            'partner_id': self.buyers_id.id,
            'move_type': 'out_invoice',
            "invoice_line_ids": [
                Command.create({
                    "name": self.name,
                    "price_unit": (self.selling_price)*0.06+100,
                    "product_id" : self.property_type_id.id,
                    "quantity" : 1,
                })
            ],
            })
        return res
