# -*- coding: utf-8 -*-
from odoo import fields, models

class estate_property(models.Model):
    _name = "estate.property"
    _description = "estate model"

    name = fields.Char(string="Name",required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer(required=True)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    #[('value','Name')]
    garden_orientation = fields.Selection([('north','North'),('east','East'),('south','South'),('west','West')])
