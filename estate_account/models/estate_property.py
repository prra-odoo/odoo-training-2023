# -*- coding: utf-8 -*-

from odoo import models, fields, Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_property_sold(self):
        for record in self:
            self.env['account.move'].create({
                'partner_id': record.buyer_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids':[
                    Command.create({
                        'name': record.name,
                        'quantity' : 1,
                        'price_unit': record.selling_price * 0.06
                    }),
                    Command.create({
                       'name': 'Administrative Fees',
                       'price_unit': 100 
                    })
                ]
            })
        return super(EstateProperty, self).action_property_sold()

'''
 Pass Values to the Child Lines of one2many Fields:
    CREATE = 0, 0,
    UPDATE = 1, ID
    DELETE = 2, ID,
    UNLINK = 3, ID
    LINK = 4, ID
    CLEAR = 5, 0, 0
    SET = (6, 0, [IDs]) will replace the current relations of existing records with the list of linked IDs,
'''
