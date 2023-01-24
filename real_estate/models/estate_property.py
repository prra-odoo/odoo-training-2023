# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare

class EstateProperty(models.Model):
    _name = "estate.property"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Real estate module properties"
    _order = "id desc"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From", default=lambda self: fields.Date.today() + relativedelta(months=+3), copy=False)
    expected_price = fields.Float(string="Expected Price", required=True, help='What is your expected price of the property?')
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False, help='What is your selling price of the property?')
    bedrooms = fields.Integer(string="Bedrooms", default=2, help="No. of Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)", help="How much Area does your Living Room contain?")
    facades = fields.Integer(string='Facades', help="The Facade is the front of the Property that is usually seen from the outside.")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)", help="How much Area does your Garden contain?", compute="_compute_garden", readonly=False)
    total_area = fields.Integer(string="Total Area (sqm)", compute="_compute_total_area", help="How much total area does your Property have?")
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], compute="_compute_garden", readonly=False)
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(string="State", readonly=True,required=True, copy=False, selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')], default="new", tracking=True)
    best_price = fields.Float(string="Best Offer", compute="_compute_best_offer", help="This will display best price from offers list.")
    property_type_id = fields.Many2one('estate.property.type', string='Type')
    buyer_id = fields.Many2one('res.partner', copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")  
    
    _sql_constraints = [
        ('expected_price_positive', 'check (expected_price > 0)', "The expected price must be strictly positive."),
        ('selling_price_positive', 'check (selling_price > 0)', "The selling price must be strictly positive."),
    ]

    # Button Methods
    
    def action_sold_btn(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError('Cancelled properties cannot be sold.')
        record.state = 'sold'
        
        # Pass this buyer data to the estate.sold.property Model
        self.env['estate.sold.property'].create(
            {
                'name': self.name,
                'postcode': self.postcode,
                'selling_price': self.selling_price,
                'property_type_id': self.property_type_id.id,
                'total_area': self.total_area,
                'buyer_id': self.buyer_id.id,
                'salesperson_id': self.salesperson_id.id
            },
        )
        return True
            
    def action_cancel_btn(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('Sold properties cannot be cancelled.')
        record.state = 'cancelled'
        return True
    
    # Method Decorators
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
           
    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for record in self:
            record.best_price =  max(record.offer_ids.mapped('price'), default=0)
            
    # @api.onchange('garden')
    # def _onchange_garden(self):
    #     for record in self:
    #         if record.garden:
    #             record.garden_area = 10
    #             record.garden_orientation = 'north'
    #         else:
    #             record.garden_area = 0
    #             record.garden_orientation = ''
    
    # Replaced onchange method with compute
    @api.depends('garden', 'garden_area', 'garden_orientation')
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0
                record.garden_orientation = ''
    
    # Python Constraints
    
    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if float_compare(record.selling_price, (0.9 * record.expected_price), precision_rounding=0.01) <= 0 and record.offer_ids:
                raise ValidationError("The selling price must be least 90% of expected price. You must have to reduce expected price if you want to accept this offer!!!")
            
    # CRUD Methods
    
    @api.ondelete(at_uninstall=False)
    def _unlink_new_cancelled(self):
        for record in self:
            if record.state not in ('new', 'cancelled'):
                raise UserError('Only new and cancelled properties can be deleted!!!')
