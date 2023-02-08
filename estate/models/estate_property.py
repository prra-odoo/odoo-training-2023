# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate_property Model"

    name = fields.Char()
    description = fields.Char()
    user_id = fields.Many2one('res.users', string='Salesperson',
                              index=True, tracking=True, default=lambda self: self.env.user)
    partner_id=fields.Many2one('res.partner',string='Buyer',index=True, tracking=True)
    property_type_id = fields.Char(required=True)
    postcode = fields.Char(required=True)
    date_availability = fields.Date(
        default=lambda self: fields.Datetime.now() + relativedelta(months=3), copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    log_access = True
    garden_orientation = fields.Selection(
        string='Garden Orientattion',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer', 'Offer'), ('recevied', 'Recevied'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        required=True,
        copy=False,
        default='new',
    )
