# -*- coding: utf-8 -*-
from odoo import fields,models,Command

class EstateOfferWizard(models.TransientModel):
    _name = "estate.offer.wizard"
    _description = "Estate Wizard for making offers to multiple Properties"

    offer_value = fields.Float(required=True)
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_ids = fields.Many2many('estate.property', default=lambda self: self.env.context.get('active_ids'))

    def action_create_offers(self):
        for record in self.property_ids:
            if(self.offer_value>=(0.9*record.expected_price) and self.offer_value>=(record.best_offer) and (record.state=="new" or record.state=="offer_received")):
                record.offer_ids = [Command.create({'partner_id':self.partner_id.id,'price':self.offer_value})]