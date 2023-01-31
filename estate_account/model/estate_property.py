# -*- coding: utf-8 -*-

from odoo import models, fields


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def property_sold(self):
        print("working")
        # print(self.check_access_rights('write')) #true
        # print(self.check_access_rule('write')) #none
        # print(" reached ".center(100, '='))
        self.env['account.move'].sudo().create({
            #'name': self.name,
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
            'invoice_date':fields.Date.context_today(self),
            'invoice_line_ids':[
                (0, self.buyer_id.id, {
                    'name': self.name,
                    'quantity': 1,
                    'price_unit': self.selling_price,
                    "tax_ids": None,
                }),
                (0, 0, {
                    'name': '6 percent of selling price',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06,
                    "tax_ids": None,
                }),
                (0, 0, {
                    'name': 'additional 100 for administrative fees.',
                    'quantity': 1,
                    'price_unit': '100',
                    "tax_ids": None,
                }),
            ],
        })
        return super().property_sold()


