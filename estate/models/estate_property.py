# -*- coding: utf-8 -*-

from odoo import models , fields

class test(models.Model):
    _name = "test.model"
    _description = "Advertisment module of real estate"
    
    
    name = fields.Char(required = True)
    postcode = fields.Char()
    description = fields.Text(required = True)
    date_availability = fields.Date("Last Availability Date",default=lambda self:fields.Datetime.now())
    expected_price = fields.Float(default = 550000)
    selling_price=fields.Float(default = 500000)
    bedrooms = fields.Integer(required = True, default = 50)
    living_area = fields.Integer(default = 2)
    facades = fields.Integer(default = 5)
    garage = fields.Boolean(default= False)
    garden_area = fields.Integer(default = 1)
    garage_orientation = fields.Selection(
        string = 'Type',
        selection=[('North','East'),('South','West')],
        help = 'Type is used to separate the Directions'
    )
    
    