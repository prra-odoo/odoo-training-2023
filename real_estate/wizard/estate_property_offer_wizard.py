# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyOfferwizard(models.TransientModel):
    _name = 'estate.property.offer.wizard'
    _description = 'Estate property offer wizard'

    # name = fields.Text(string='Name')
    price = fields.Float('Price',required=True,default=0)
    partner_id = fields.Many2one('res.partner',required=True)
    offer_ids = fields.One2many('estate.property.offer','property_id')
    
    # Wizard Button Method
    
    def make_an_offer(self):
        active_ids = self._context.get('active_ids')
        print('------------------------------')
        print(active_ids)
        
        for property_id in active_ids:
            property = self.env['estate.property'].browse(property_id)
            # print(property.mapped('name'))
            
            property.write({
                "offer_ids": [
                    fields.Command.create({
                        "price": self.price,
                        "partner_id": self.partner_id.id,
                    })
                ],
            })
    