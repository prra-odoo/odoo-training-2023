# -*- coding:utf-8 -*-
from odoo import models, fields, Command

class PropertyOfferWizard(models.TransientModel):
	_name = 'property.offer.wizard'

	offer_amount = fields.Float(string='Offer Amount')
	buyer_id = fields.Many2one('res.partner',string='Buyer',index=True)
	status = fields.Char()

	def send_offer(self):
		sel_properties = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        # sel_properties = self.env['estate.property'].search([
    	# 	('state', 'in', ['new', 'offer_recieved']),
    	# 	('expected_price', '==', 500000)
		# 	]).browse(self.env.context.get('active_ids'))
		for record in sel_properties:
			if(record.state in ['new','offer_recieved'] and record.expected_price <= 500000 and record.property_type_id.name == 'Home'):
				record.write({
					'offer_ids':[
					Command.create({
						'price':self.offer_amount,
						'buyer_id':self.buyer_id.id
						})
					]
					})
				return {'type': 'ir.actions.act_window_close'}
