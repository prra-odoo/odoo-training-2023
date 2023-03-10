# -*- coding: utf-8 -*-

from odoo import fields, models, Command


class EstatePropertyWizard(models.TransientModel):
    _name = 'estate.property.wizard'
    _description = "Estate Property Wizard"

    price = fields.Float(string="Offer Price")
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    # status = fields.Char()

    def action_make_offer(self):
        properties = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        for record in properties:
            if(record.state in ['new','offer_received'] and record.expected_price == 500000 and record.property_type_id.name == 'Apartment'):
                record.write({
                    'offer_ids':[
                    Command.create({
                        'price':self.price,
                        'partner_id':self.buyer_id.id
                        })
                    ]
                })
        return {'type': 'ir.actions.act_window_close'}