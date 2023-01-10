# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.tools.date_utils import add,subtract
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError


class esattePropertyOffer(models.Model):
	_name="estate.property.offer"
	_description="This model defines the estate property offers"
	_order = "price desc"
	
	price=fields.Float("Offer Price")
	status=fields.Selection(
		string="Status",
		selection=[('accepted','Accepted'),('refused','Refused')], copy=False)
	partner_id=fields.Many2one('res.partner',required=True,string="Buyer")
	property_id=fields.Many2one('estate.property',required=True)
	validity=fields.Integer("Validity",default='7')
	create_date=fields.Date(default=lambda self: fields.datetime.today())
	date_deadline=fields.Date("Date deadline",default=fields.datetime.today(),compute='_compute_deadline_date',inverse='_inverse_deadline_date')
	property_type_id = fields.Many2one("estate.property.type",related = "property_id.property_type_id",store=True,string="Property Type")

	_sql_constraints=[
	('offer_price_check','CHECK(price>0)','Offer Price is strictly positive'),]

	#compute fields
	@api.depends('create_date','validity')
	def _compute_deadline_date(self):
		for record in self:
			record.date_deadline=record.create_date+relativedelta(days=record.validity)
			# record.date_deadline=record.create_date+ timedelta(days=record.validity)

	def _inverse_deadline_date(self):
		for record in self:
			record.validity=(record.date_deadline -record.create_date).days

	def accepted_action(self):
			if self.property_id.selling_price==0:
				self.property_id.selling_price = self.price
				self.property_id.buyer_id = self.partner_id
				self.status = "accepted"
				self.property_id.state= "offer_accepted"
		return True

	def refused_action(self):
		for record in self:
			record.status = "refused"
		return True

	

			