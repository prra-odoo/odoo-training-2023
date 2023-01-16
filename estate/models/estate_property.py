# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

class estate_property(models.Model):
    _name = "estate.property"
    _description = "estate model"

    name = fields.Char(string="Name",required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string="Available From",default=fields.Date.today()+relativedelta(months=+3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(string="Selling Price",readonly=True,copy=False)
    bedrooms = fields.Integer(string="Bedrooms",default=2)
    living_area = fields.Integer(required=True)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    #[('value','Name')]
    garden_orientation = fields.Selection([('north','North'),('east','East'),('south','South'),('west','West')])
