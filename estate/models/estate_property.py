from odoo import models,fields

from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
	_name='estate.property'
	_description='demo model with property trsting'

	name=fields.Char(string='Name',
			required=True,
			help="this is for name")

	discription=fields.Char(string='Discription',
			help="this is for discription",
			size=300)

	postcode=fields.Char(string='Postcode',
			help="this is for postcode")

	date_availability=fields.Date(string='Availabe From',
			help="this is for data availibility",
			copy=False,
			default=lambda self:fields.Date.today()+relativedelta(months=+3))

	expected_price=fields.Float(string='Expected Price',
			required=True,
			help="this is for expeccted price")

	selling_price=fields.Float(string='Selling Price',
			help="this is for selling price",
			readonly=True,
			copy=False)

	bedrooms=fields.Integer(string='Bedrooom',
			default=2,
			help="this is for bedroom")

	living_area=fields.Integer(string='Living Area(sqm)',
			help="this is for living area")

	facades=fields.Integer(string='Facades',
			help="this is for facades")

	garage=fields.Boolean(string='Garbage',
			help="this is for garage")

	garden=fields.Boolean(string='Garden',
			help="this is for garden")

	garden_area=fields.Integer(string='Garden area',
			help="this is for garden area")

	garden_orientation=fields.Selection(selection = [('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')],
        string= "Garden Orientation",)

	Active=fields.Boolean(default=True)

	state=fields.Selection(selection=[('new','New'),('offer received','Offer Received'),
		('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
		required=True,
		copy=False,
		default='new',
		string="status")

	property_type_id=fields.Many2one('estate.property.type',
		string="Property_Type")
	buyer_id=fields.Many2one('res.users',
		string="Buyer",
		copy=False)
	salesperson_id=fields.Many2one('res.partner',
		string="Salesman",
		default=lambda self: self.env.user)

	tag_ids=fields.Many2many('estate.property.tag',
		string="Tags")
	offer_ids=fields.One2many('estate.property',
		'partner_id',
		string="Offer")