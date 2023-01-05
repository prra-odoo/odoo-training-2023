# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero


class realEstate(models.Model):
    _name = "real.estate"
    _description = "This is regarding the real_estate"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Integer(string='Postcode')
    date_availability = fields.Date(
        string='Date Available', default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(string=' Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', required=True)
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type" )
    salesperson_id = fields.Many2one(
        "res.users", string="Salesperson", default=lambda self: self.env.user, copy=False)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')]
    )
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")
    offer_ids = fields.One2many(
        "estate.property.offer", "property_id", string="Estate Offer")
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[('new', 'New'),
                                        ('offer_received', 'Offer Received'),
                                        ('offer_accepted', 'Offer Accepted'),
                                        ('sold', 'Sold'), ('cancel', 'Cancelled')], default='new', required=True
                             )
    total_area = fields.Integer(string='Total Area', compute="_compute_total")
    best_offer = fields.Float(
        string='Best Offer', compute="_compute_best_offer")

    status = fields.Selection(
        selection=[('sold', 'Sold'), ('cancel', 'Cancel')], tracking=True)

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(self.offer_ids.mapped('price'), default=0)

    def sold_button(self):
        for record in self:
            if record.status == 'cancel':
                raise UserError(('Cancelled property can not be sold.'))
            else:
                record.status = 'sold'

    def cancel_button(self):
        for record in self:
            if record.status == 'sold':
                raise UserError(('Sold property can not be sold.'))
            else:
                record.status = 'cancel'

    _sql_constraints = [('expected_price', 'CHECK(expected_price>=0)', 'Expected Price should be positive'),
                        ('selling_price', 'CHECK(selling_price>=0)',
                         'Selling Price should be positive')
                        ]

    @api.constrains("expected_price", "selling_price")
    def _price_difference(self):
        for record in self:
            if ((not float_is_zero(record.selling_price, precision_rounding=0.01))
                    and float_compare(record.selling_price, record.expected_price*0.9, precision_rounding=0.01) < 0
                    ):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price!"
                )
