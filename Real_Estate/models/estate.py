
# -*- coding: utf-8 -*-
from odoo import fields, models

class realEstate(models.Model):
    _name = "estate_model"
    _description = "Estate Model"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    garder_orientation = fields.Selection(string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')],
        help="Type is used to separate Leads and Opportunities")
    