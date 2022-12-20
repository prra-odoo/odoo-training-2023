# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateModel(models.Model):
    _name = "estate.model"
    _description = "Estate Model"

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_avilability = fields.Date()
    expected_price = fields.Float(required = True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
        )
