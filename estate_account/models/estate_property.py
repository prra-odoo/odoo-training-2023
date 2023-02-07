# -*- coding: utf-8 -*-


from odoo import models, Command


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def sold_buisness_logic(self):
        # self.env["estate.property"]
        # breakpoint()

        self.env['account.move'].create({
            'name': 'Estate Property',
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
            # 'invoice_date': '2019-01-21',
            # 'date': '2019-01-21',
            # 'invoice_line_ids': [(0, 0, {
            # 'product_id': self.id,
            # 'price_unit': self.selling_price,
            # 'tax_ids': [],
            # })],
            'invoice_line_ids': [Command.create({
                'name': self.name,
                'price_unit': (self.selling_price*.06),
                'quantity': 1,   
            }),
            Command.create({
                'name': 'Administrative Fees',
                'price_unit': 100.0,
                'quantity': 1,
            })],
            
        })
        

        return super().sold_buisness_logic()
