# -*- coding: utf-8 -*-
from odoo import fields, models, Command


class EstateProperty(models.Model):
	_inherit = 'estate.property'

	def action_sold(self):
		self.env['account.move'].create({
			'partner_id': self.buyer_id.id,
			'move_type': 'out_invoice',
			# 'name': 'Property',
            'invoice_line_ids': [
                Command.create({
                	'name': self.name,
                	'quantity': 1,
                	'price_unit': self.selling_price,

                }),
                Command.create({
                	'name': 'Charge',
                	'quantity': 1,
                	'price_unit': self.selling_price * 0.06,

                }),
                Command.create({
                	'name': 'Administrative fees',
                	'quantity': 1,
                	'price_unit': 100,

                })
              ],
			})

		return super(EstateProperty,self).action_sold()