# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.tools.float_utils import float_compare, float_is_zero
import re


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property Model"
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'new.estate']

    name = fields.Char(required=True)
    description = fields.Text()
    user_id = fields.Many2one('res.users', string='Salesperson',
                              index=True, default=lambda self: self.env.user, tracking=True)
    partner_id = fields.Many2one(
        'res.partner', string='Buyer', index=True, readonly=True, tracking=True)
    property_type_id = fields.Many2one(
        'estate.property.type', index=True)
    property_tag_id = fields.Many2many(
        'estate.property.tag', relation='tag_connection')
    postcode = fields.Char(required=True)
    date_availability = fields.Date(
        default=lambda self: fields.Datetime.now() + relativedelta(months=3), copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False, tracking=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(
        compute='_compute_garden', readonly=False, store=True)
    total_area = fields.Integer(
        compute="_compute_total_area", string="Total Area")
    best_offer = fields.Float(
        compute="_compute_best_offer", string="Best Offer", tracking=True)
    garden_orientation = fields.Selection(
        string='Garden Orientattion',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')], compute='_compute_garden', readonly=False, store=True
    )
    priority = fields.Selection(
        selection=[('0', 'low'), ('1', 'high')]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer_received', 'Offer received'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        required=True,
        copy=False, tracking=True
    )
    kanban_state = fields.Selection(
        selection=[('new', 'grey'), ('offer_received', 'blue'), ('offer_accepted', 'yellow'),
                   ('sold', 'green'), ('cancelled', 'red')]
    )
    offers_id = fields.One2many('estate.property.offer', 'property_id')
    property_image = fields.Binary()

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('offers_id')
    def _compute_best_offer(self):
        for record in self:
            if (record.offers_id):
                if record.state == "new":
                    record.state = "offer_received"
            else:
                record.state = "new"
            record.best_offer = max(record.mapped(
                'offers_id.price'), default=0)

    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_orientation = 'north'
                record.garden_area = 10
            else:
                record.garden_orientation = None
                record.garden_area = 0

    def action_sold(self):
        for record in self:
            if record.state != "sold":
                record.state = "sold"
        return True

    def action_cancel(self):
        for record in self:
            if record.state != "cancelled":
                record.state = "cancelled"
        return True

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)',
         'Expectted Price must be positive.'),
        ('check_selling_price', 'CHECK(selling_price >= 0)',
         'Selling Price must be positive')
    ]

    @api.constrains("selling_price")
    def _check_offer_price(self):
        for record in self:
            sp = (90*record.expected_price)/100
            if ((not float_is_zero(record.selling_price, precision_rounding=0.01)) and
                    float_compare(sp, record.selling_price, precision_rounding=0.01) >= 0):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price! You must reduce the expected price if want to accept this offer")

    # @api.constrains('name')
    # def valid_name(self):
    #     for record in self:
    #         if not re.match(r'^[a-zA-Z ]+$', record.name):
    #             raise ValidationError("Invalid property name.")

    @api.ondelete(at_uninstall=False)
    def _unlink_except_state_new_received(self):
        for record in self:
            if record.state not in ['new', 'cancelled']:
                raise UserError("Can't delete this property!")
