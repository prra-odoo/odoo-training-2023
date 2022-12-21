# -*- coding: utf-8 -*-

from odoo import models, fields
import datetime

class EstateModel(models.Model):
    _name = "estate.model"
    _description = "Estate Model"

    name = fields.Char(required = True, readonly = True)
    description = fields.Text()
    postcode = fields.Char()
    date_avilability = fields.Date('date availability', default = lambda self: self.datetime.now())
    expected_price = fields.Float('expected price', required = True)
    selling_price = fields.Float('selling price', copy = False)
    bedrooms = fields.Integer()
    living_area = fields.Integer('living area')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('garden area')
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
        )
