# -*- coding: utf-8 -*-

from odoo import models,Command

class estateProperty(models.Model):
    _inherit= "estate.property"
    
    def action_sold(self):
        self.env['account.move'].create(
            {
                'partner_id': self.buyers_id.id,
                'move_type' : 'out_invoice',
                'invoice_line_ids' : [
                    Command.create({
                        'name' : self.name,
                        'quantity' : 1,
                        'price_unit' : 0.94*self.selling_price
                    }),
                    Command.create({
                        'name' : self.name,
                        'quantity' : 2,
                        'price_unit' : 100
                    })
                ]
                
            }
        )
        return super(estateProperty,self).action_sold()
    