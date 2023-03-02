# -*- coding: utf-8 -*-
from odoo import models, Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        # breakpoint()
        # print('in acount estate')

        self.env['account.move'].create(
            {
            'partner_id':self.buyer_id.id,
            'move_type': 'out_invoice',
            'line_ids': [
                    Command.create({
                        'name': self.name,
                        'quantity': 1,
                        'price_unit': self.selling_price,
                    }),
                    Command.create({
                        'name': 'Invoice Charge',
                        'quantity': 1,
                        'price_unit': self.selling_price * 0.06,
                    }),
                    Command.create({
                        'name': 'Administrative Fee',
                        'quantity': 1,
                        'price_unit': 100,
                    })]
            })
        return super(EstateProperty,self).action_sold()