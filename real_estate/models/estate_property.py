# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a regarding Real Estate"
    active = fields.Boolean(default=True)
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    # Fields
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Datetime.now() + relativedelta(months=3), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(required=True, default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    state = fields.Selection(
        selection = [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',
        tracking=True
    )

    # Relational Fields
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False, readonly=True)
    salesperson_id = fields.Many2one('res.users', string="Sales Person", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offer")

    # Computed Fields
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer = fields.Float(compute="_compute_best_offer", default=0)

    # SQL Constraints
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'The expected Price must be strictly positive!'),
        ('check_selling_price', 'CHECK(selling_price >=0)', 'The Selling Price must be positive!')
    ]

    # Computed Methods
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price'), default=0)

    # Action Methods
    def action_property_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Canceled Properties cannot be sold")
            record.state = 'sold'
        return True

    def action_property_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold Properties cannot be canceled")
            record.state = 'canceled'
        return True

    # Python Constraints
    @api.constrains('expected_price', 'selling_price')
    def _check_expected_price(self):
        for record in self:
            if not float_is_zero(record.selling_price, precision_digits = 2) and float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
                raise ValidationError("The selling price must be 90 % of Expected Price")

    @api.ondelete(at_uninstall=False)
    def _prevent_deletion(self):
        for record in self:
            if record.state != 'new' and record.state != 'canceled':
                raise UserError("Only New and Canceled Properties can be deleted!")

    # def unlink(self):
    #     for record in self:
    #         if record.state != 'new' and record.state != 'canceled':
    #             raise UserError("Only New and Canceled Properties can be deleted!")
    #     return super().unlink()
