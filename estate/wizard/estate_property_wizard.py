# -*- coding: utf-8 -*-

from odoo import models, fields ,Command


class EstatePropertyWizard(models.TransientModel):
    _name = "estate.property.wizard"
    _description = "new"

    price = fields.Float()
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)

    def action_done_wizard(self):
        records = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        for rec in records: 
            rec.write({
                'offer_ids': [
                    Command.create({
                        'price':self.price,
                        'partner_id':self.partner_id.id,
                    })
                ]
                })

        
