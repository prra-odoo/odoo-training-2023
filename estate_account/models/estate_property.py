# -*- coding: utf-8 -*-

from odoo import models,fields,Command

class estateInvoice(models.Model):
	_inherit ='estate.property'

	def sold_button(self):
		
		# journal = self.env["account.journal"].sudo().search([("type", "=", "sale")], limit=1)
		if self.env['account.move'].check_access_rights('write') and self.env['account.move'].check_access_rule('write'):
			print(" reached ".center(100, '='))
		for record in self:
			
			self.env['account.move'].sudo().create(
				{
					"partner_id":record.buyer_id.id,
					"move_type":'out_invoice',
					# "journal_id": journal.id,
					"invoice_line_ids":
					[
						Command.create({
							"name":record.name,
							"quantity":1,
							"price_unit":record.selling_price *0.06
							}),
						Command.create({
							"name":record.name,
							"price_unit":100
							}),
					]
				})
		return super().sold_button()
