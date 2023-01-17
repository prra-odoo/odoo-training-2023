# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import date
from dateutil.relativedelta import relativedelta


class estate_property(models.Model):
    _name = "estate.property"
    _description = "estate model"

    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From", default=fields.Date.today()+relativedelta(months=+3), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')])
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('done', 'Done'),
        ('cancel', 'Cancel'), ], string='State', default='new', copy=False)
    property_type = fields.Many2one("estate.property.type",string="Property Type")
    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user) 
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Property tag")
    offer_ids = fields.One2many('estate.property.offer','property_id',string="offer")
