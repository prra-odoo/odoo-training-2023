# -*- coding: utf-8 -*-

from odoo import models, fields

class estateModel(models.Model):
    _name = "estate.model"
    _description = "Real Estate Module"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garage_orientation = fields.Selection(
        string='Type',
        selection=[('east', 'East'), ('west', 'West'),('north','North'),('south','South')],
        help="Type is used to separate Leads and Opportunities")
