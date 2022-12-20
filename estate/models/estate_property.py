# -*- coding: utf-8 -*-

from odoo import models , fields

class test(models.Model):
    _name = "test.model"
    _description = "Advertisment module of real estate"
    
    
    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms = fields.Integer()
    living_areas = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Type',
        selection=[('North','East'),('South','West')],
        help = 'Type is used to separate the Directions'
    )
    
    