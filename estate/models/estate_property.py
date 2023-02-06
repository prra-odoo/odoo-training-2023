from odoo import models,fields

class Estate_Property(models.Model):
	_name='estate.property'
	_description='demo model with property trsting'

	name=fields.Char(string='name',
			required=True,
			help="this is for name")

	discription=fields.Text(string='discription',
			help="this is for discription")

	postcode=fields.Char(string='postcode',
			help="this is for postcode")

	date_availability=fields.Date(string='date availability',
			help="this is for data availibility")

	expected_price=fields.Float(string='expected price',
			required=True,
			help="this is for expeccted price")

	selling_price=fields.Float(string='selling price',
			help="this is for selling price")

	bedrooms=fields.Integer(string='bedrooom',
			help="this is for bedroom")

	living_area=fields.Integer(string='living area',
			help="this is for living area")

	facades=fields.Integer(string='facades',
			help="this is for facades")

	garage=fields.Boolean(string='garbage',
			help="this is for garage")

	garden=fields.Boolean(string='garden',
			help="this is for garden")

	garden_area=fields.Integer(string='garden area',
			help="this is for garden area")

	garden_orientation=fields.Selection(selection = [('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')],
        string= "Garden Orientation",)

