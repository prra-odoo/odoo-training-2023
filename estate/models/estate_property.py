# -*- coding: utf-8 -*-

from odoo import models,fields

class estateProperty(models.Model):
    _name = "estate.property"
    
    _description = "This is the description of the property"


    heading=fields.Char()
    name = fields.Char(required=True)
    id = fields.Integer()
    postcode = fields.Char()
    description = fields.Text(copy=False)
  
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=4)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )

