# -*- coding: utf-8 -*-
from odoo import models,fields

class Estate_Property(models.Model):
    _name = "estate.property"
    _description = "Property Model"

    name = fields.Char(string = 'name',required=True)
    description = fields.Text(string = 'description')
    postcode = fields.Char(string = 'postcode', required = True)
    data_avabilability = fields.Date('Datetime')
    expected_price = fields.Float(string = 'expected price',required = True)
    selling_price = fields.Float(string = 'selling price')
    bedrooms = fields.Integer(string = 'bedrooms')
    living_area = fields.Integer(string = 'living area')
    facades = fields.Integer(string = 'facades')
    garage = fields.Boolean(string = 'garage')
    garden_area = fields.Integer(string = 'garden area')
    garden_orientation = fields.Selection(
        string = 'garden orientation',
        selection = [('north','North'),('south','South'),('east','East'),('west','West')]
    )
