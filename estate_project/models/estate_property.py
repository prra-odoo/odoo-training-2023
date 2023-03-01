# -*- coding: utf-8 -*-
from odoo import fields, models, Command


class EstateProperty(models.Model):
	_inherit = 'estate.property'

	def action_sold(self):
		self.env['project.project'].create({
			'name': self.name,
			'partner_id': self.buyer_id.id,
			'task_ids': [
                Command.create({
                	'name': 'Maintenance',
                	'partner_id': self.buyer_id.id,
                })
               ],
   			 }) 
		return super(EstateProperty,self).action_sold()