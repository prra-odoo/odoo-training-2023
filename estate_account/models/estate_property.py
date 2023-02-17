# -*- coding: utf-8 -*-


from odoo import models, Command


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def sold_buisness_logic(self):

        self.env['account.move'].create({
            'name': 'Estate Property',
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
            'invoice_line_ids': [Command.create({
                'name': self.name,
                'price_unit': (self.selling_price*.06),
                'quantity': 1,'tax_ids':None
            }),
            Command.create({
                'name': 'Administrative Fees',
                'price_unit': 100.0,
                'quantity': 1,'tax_ids':None
            })
            ]
            })
        self.env['project.project'].create({
            'name': self.name,
            'task_ids': [(0, 0, {
                'name': "Cleaning",
            })]
        })
        return super().sold_buisness_logic()
