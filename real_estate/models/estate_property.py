# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.tools.date_utils import add

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a regarding Real Estate"
    active = fields.Boolean(default=True)

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: add(fields.Datetime.now(), months=3), copy=False)
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
        default='new'
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer = fields.Many2one('res.partner', string="Buyer", copy=False)
    sales_person = fields.Many2one('res.users', string="Sales Person", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    