from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class realProperty(models.Model):
    _name = "estate.real.property"
    _description = "Real estate model"
    _sql_constraints = [
        ('expected_price_check', "CHECK(expected_price > 0 and expected_price != 0)",
         "Expected Price must be positive."),
        ('selling_price_check', "CHECK(selling_price>0)",
         "Selling Price must be positive")

    ]

    @api.constrains('expected_price', 'selling_price')
    def _selling_price(self):
        for record in self:
            if not float_is_zero(record.expected_price,precision_digits=2) and not float_is_zero(record.selling_price,precision_digits=2):
                if float_compare(record.selling_price, record.expected_price * 0.9,precision_digits=2) == -1:
                    raise ValidationError(
                        "selling price cannot be less than 90% the expected price")

    name = fields.Char(default="unknown")
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Datetime(
        default=datetime.now() + relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(
        compute="_compute_garden", store=True, readonly=False)
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
        help="Select an appropriate direction",
        compute="_compute_garden", store=True, readonly=False)
    active = fields.Boolean()
    state = fields.Selection(string='State',
                             selection=[('new', 'New'), ('recieved', 'Offer Recieved'), (
                                 'accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
                             help="select the state")
    property_type_id = fields.Many2one(
        "estate.property.type", name="Property Type")
    buyer_id = fields.Many2one("res.partner", name="Buyer", copy=False)
    seller_id = fields.Many2one(
        "res.users", name="Salesman", default=lambda self: self.env.user)
    tag_ids = fields.Many2many(
        "estate.property.tag", string="Tags", relation='tag_ids_m2m')
    offer_ids = fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_id',
        string='Offers',
        required=True
    )
    total_area = fields.Float(compute='_compute_total')

    @api.depends('garden_area', 'living_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.garden_area+record.living_area
    description_buyer = fields.Char(compute='_compute_description_buyer')

    @api.depends('buyer_id.name')
    def _compute_description_buyer(self):
        for record in self:
            record.description_buyer = record.buyer_id.name
    best_price = fields.Float(compute='_compute_best_price')

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if (record.offer_ids):
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0
    """ @api.onchange('garden')
    def onchange_check_garden(self):
        if self.garden==True:
            self.garden_area=10
            self.garden_orientation='north'
        else:
            self.garden_area=0
            self.garden_orientation="" 
   
    @api.depends('garden')
    def _compute_inverse_garden(self):
        for record in self:
            if record.garden==True:
                record.garden_area=10
                record.garden_orientation='north'
            else:
                record.garden_area=0
                record.garden_orientation=''  """
    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if (record.garden == True):
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0
                record.garden_orientation = ''

    def action_sold(self):
        for record in self:
            if (record.state == 'cancelled'):
                raise UserError(("Cancelled property cannot be sold."))
            else:
                record.state = 'accepted'

    def action_cancelled(self):
        for record in self:
            record.state = 'cancelled'


"""  def _compute_button_class(self):
        for record in self:
            if record.status == 'sold':
                record.button_class = 'oe_highlight' """
