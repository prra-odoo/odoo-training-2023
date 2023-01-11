# -*- coding: utf-8 -*-
from odoo import api,fields,models,exceptions
from datetime import date
from dateutil.relativedelta import relativedelta
class real_Esate_Properties(models.Model):

	_name='real.estate.properties'
	_description="Property Details"


	name=fields.Char(required=True,default="Unknown")
	description=fields.Text()
	Postcode=fields.Char()
	date_availablity=fields.Date(copy=False,default=fields.date.today()+relativedelta(months=3))
	expected_price=fields.Float(required=True)
	selling_price=fields.Float(readonly=True,copy=False)
	bedroom=fields.Integer(default="2")
	living_area=fields.Integer(string="Living Area (sqm)")
	facades=fields.Integer()
	garage=fields.Boolean()
	gardan=fields.Boolean(string="Garden")
	gardan_area=fields.Integer(string="Garden Area (sqm)",compute="_compute_gardan",readonly=False)
	garden_orientation=fields.Selection(
		string='Orientation',
		selection=[('north','North'),('south','South'),('east','East'),('west','West')],
		# compute="_compute_gardan",
		readonly=False
	)
	active=fields.Boolean(default=True)
	state=fields.Selection(
		string='State',
		selection=[('new','New'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancled','Canceled')],
		required=True,
		copy=False,
		default='offer_recieved'
	)
	property_type_id=fields.Many2one("estate.property.type")
	buyer=fields.Many2one("res.partner",copy=False,readonly=True)
	salesperson=fields.Many2one("res.users",default=lambda self: self.env.user)
	tag_ids=fields.Many2many("estate.property.tag",relation="property_and_tag_id",column1="property_id",column2="tag_id")
	offer_ids=fields.One2many("estate.property.offer","property_id")
	total_area=fields.Float(compute="_total_area")
	best_price=fields.Float(compute="_best_price",default=0)

	@api.depends("living_area","gardan_area")
	def _total_area(self):
		for area in self:
			area.total_area=area.living_area+area.gardan_area

	@api.depends("offer_ids.price")
	def _best_price(self):
		for value in self:

			value.best_price=max(value.offer_ids.mapped('price'),default=0)
			
			# temp=(l.price for l in value.offer_ids)   without mapped
			# value.best_price=max(temp,default=0)

	def action_sold(self):
		for action in self:
			if action.state != 'cancled':
				action.state='sold'
			else:
				raise exceptions.UserError("You cannot sold cancled property")

	def action_cancel(self):
		for action in self:
			if action.state != 'sold':
				action.state="cancled"
			else:
				raise exceptions.UserError("You cannot cancled sold property")

	@api.depends("gardan")
	def _compute_gardan(self):
		for record in self:
			if record.gardan == True:
				record.gardan_area="10"
				record.garden_orientation="north"
			else:
				record.gardan_area="0"
				record.garden_orientation=""
	
	_sql_constraints = [
        ('expected_price','CHECK(expected_price>0)','price cannot be negative or zero')
    ]			
    