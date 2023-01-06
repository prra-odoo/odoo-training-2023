# -*- coding: utf-8 -*-

from odoo import api,models,fields
from datetime import date
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_compare, float_is_zero

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "The Real Estate Advertisement Module"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _order = "id desc"

    name = fields.Char(string='Name', required=True, copy=True)
    description = fields.Text(string='Description')
    postcode = fields.Integer(string='Postcode')
    date_availability = fields.Date(string='Available From', default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden=fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation',
        selection=[('east', 'East'), ('west', 'West'), ('north', 'North'), ('south', 'South')]
        )
    state = fields.Selection(selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancel', 'Cancel')],
                                        default='new'
        )
    active = fields.Boolean(default = True)
    property_type_id = fields.Many2one("estate.property.type", string='Property Type')
    buyer_id = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesman_id = fields.Many2one("res.users",string="Salesperson", default=lambda self: self.env.user )
    tag_ids=fields.Many2many("estate.property.tag", string='Tags')
    offer_ids=fields.One2many("estate.property.offer","property_id", string="Offer")
    total_area=fields.Float(string="Total Area", compute="_compute_total")
    best_offer=fields.Float(string="Best Offer",compute="_compute_best_offer")
    status=fields.Selection(string="Status", selection=[("sold", "Sold"), ("cancel", "Cancel")], tracking=True)

    _sql_constraints = [
        ('expected_price', 'CHECK(expected_price >= 0)', 'A property expected price should be positive.'),
        ('selling_price', 'CHECK(selling_price >= 0)', 'A property selling price should be positive.')
    ]

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(self.offer_ids.mapped('price'), default=0)

    def sold_button(self):
        for record in self:
            if record.status=='cancel':
                raise UserError(('Cancelled property can not be sold.'))
            else:
                record.status = 'sold'

    def cancel_button(self):
        for record in self:
            if record.status=='sold':
                raise UserError(('Sold property can not be sold.'))
            else:
                record.status = 'cancel'

    @api.constrains("expected_price", "selling_price")
    def _check_price_difference(self):
        for record in self:
            if (not float_is_zero(record.selling_price, precision_rounding=0.01) and float_compare(record.selling_price, record.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0):
                raise ValidationError("The selling price must be at least 90% of the expected price! "
                                        + "You must reduce the expected price if you want to accept this offer.")
