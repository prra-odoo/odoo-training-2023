# -*- coding: utf-8 -*-
from odoo import fields,models
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
	gardan_area=fields.Integer(string="Garden Area (sqm)")
	garden_orientation=fields.Selection(
		string='Orientation',
		selection=[('north','North'),('south','South'),('east','East'),('west','West')]
	)
	active=fields.Boolean(default=True)
	state=fields.Selection(
		string='State',
		selection=[('new','New'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancled','Canceled')],
		required=True,
		copy=False,
		default='offer_recieved'
	)
	type_id=fields.Many2one("estate.property.type",)

		
	


