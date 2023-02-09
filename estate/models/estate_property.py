# -*- coding: utf-8 -*-
from odoo import fields, models
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string='Availability Date', default=lambda self: fields.Date.today()+relativedelta(months=+3), copy=False)
    expected_price = fields.Float(string='Expected Price',required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        selection = [('north', 'North'), ('east', 'East'),
                   ('south', 'South'), ('west', 'West')]
    )
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        selection = [('new','New'),
                     ('offer_received','Offer Received'),
                     ('offer_accepted','Offer Accepted'),
                     ('sold','Sold'),
                     ('canceled','Canceled')], string='State', default="new", copy=False)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tag")