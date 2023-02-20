# -*- coding: utf-8 -*-
from odoo import fields,models,api,Command

class estatePropertyWizard(models.TransientModel):
    _name =  "estate.property.wizard"
    _description = "Real Estate Wizard"
    
    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', copy=False, 
                    selection=[('accepted', 'Accepted'),('refused', 'Refused')]
                    )
    partner_id = fields.Many2one("res.partner", string="Partner", copy=False)

    def make_an_offer(self):
        result = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        for record in result:
            record.write({
                'offer_ids':[
                    Command.create({
                        'price':self.price,
                        'partner_id':self.partner_id.id
                    })  
                ]
            })  
