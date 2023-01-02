from odoo import fields,models

class real_Esate_Properties(models.Model):

	_name='real.state.properties'
	_description="Selling your properties"


	name=fields.Char(required=True)
	description=fields.Text()
	Postcode=fields.Char()
	date_availablity=fields.Date()
	expected_price=fields.Float(required=True)
	selling_price=fields.Float()
	bedroom=fields.Integer()
	living_area=fields.Integer()
	facades=fields.Integer()
	garage=fields.Boolean()
	gardan=fields.Boolean()
	gardan_area=fields.Integer()
	garden_orientation=fields.Selection(
		string='Orientation',
		selection=[('1','North'),('2','South'),('3','East'),('4','West')])
	
	
