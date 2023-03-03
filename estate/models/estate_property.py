from odoo import api,models,fields
import odoo.exceptions
from dateutil.relativedelta import relativedelta
from odoo.tools.float_utils import float_is_zero,float_compare

class EstateProperty(models.Model):
	_name='estate.property'
	_inherit="model.test"
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description='demo model with property trsting'
	_order="id desc"

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
			default=0)

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
			help="this is for garden area",
			compute="_compute_value",
			store=True,
			readonly=False)

	garden_orientation=fields.Selection(selection = [('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')],
        string= "Garden Orientation",
		compute="_compute_value",
		store=True,
		readonly=False)

	Active=fields.Boolean(default=True)

	state=fields.Selection(selection=[('new','New'),('offer received','Offer Received'),
		('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
		required=True,
		copy=False,
		default='new',
		string="status",
		readonly=False,
		store=True,
		compute="_compute_receive",
		tracking=True)
	#for state validation
	stage_id2=fields.Selection(related='state')

	property_type_id=fields.Many2one('estate.property.type',
		string="Property_Type")
	buyer_id=fields.Many2one('res.partner',
		string="Buyer",
		copy=False)
	salesperson_id=fields.Many2one('res.users',
		string="Salesman",
		default=lambda self: self.env.user)

	tag_ids=fields.Many2many('estate.property.tag',
		string="Tags",relation="estate_tag")
	offer_ids = fields.One2many("estate.property.offer", "property_id", string="Tests")

	total_area=fields.Integer(compute="_total_sum",
		string="Total Area(sqm)")

	@api.depends("living_area","garden_area")
	def _total_sum(self):
		for record in self:
			record.total_area=record.living_area+record.garden_area

	best_price=fields.Float(compute="_offer_price",string="Best Offer")

	@api.depends("offer_ids.price")
	def _offer_price(self):
		for record in self:
			if record.offer_ids:
				record.best_price = max(record.offer_ids.mapped('price'))
			else:
				record.best_price=0
	@api.depends("garden")
	def _compute_value(self):
		for record in self:
			if record.garden==True:
				record.garden_area=10
				record.garden_orientation="north"
			else:
				record.garden_area=False
				record.garden_orientation=False

	def action_sold(self):
		for record in self:
			if record.state=="canceled":
				raise odoo.exceptions.UserError('Canceled properties can not be sold')
			else:
				record.state="sold"

	def action_cancle(self):
		for record in self:
			if record.state=="sold":
				raise odoo.exceptions.UserError('Sold properties can not be canceled')
			else:
				record.state="canceled"
	_sql_constraints=[
		('chech_price','CHECK (expected_price>0 and selling_price>=0)','Expected peice must be positive.')
	]


	'''@api.constrains('expected_price','selling_price')
	def check_exp_price(self):
		for record in self:
			if not float_is_zero(record.expected_price,precision_digits=2) and not float_is_zero(record.selling_price,precision_digits=2):
				if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
					raise odoo.exceptions.ValidationError("selling price must not be lower than 90 persent of exception price.")'''
	@api.depends('offer_ids')
	def _compute_receive(self):
		if self.offer_ids:
			self.state="offer received"

	user_id=fields.Many2one("res.users")

	@api.ondelete(at_uninstall=False)
	def _unlink_property(self):
		for record in self:
			if record.state not in ('new','canceled'):
				raise odoo.exceptions.AccessError("only properties with stage sold and cancle are deleted.")

	
		
		

class ResUser(models.Model):
	_inherit="estate.property"

	price=fields.Float()
	date=fields.Date()
	facecode=fields.Char()
