
# -*- coding: utf-8 -*-
from odoo import fields, models

class realEstate(models.Model):
    _name = "estate.model"
    _description = "Estate Model"

    name = fields.Char('name', required = True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode' ,required= True)
    date_availability = fields.Date('Date', default=lambda self: fields.Datetime.now())
    expected_price = fields.Float('Expected price')
    selling_price = fields.Float('Seling price' , default = '20000', copy = False)
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage' , readonly=True)
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden area')
    garder_orientation = fields.Selection(string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')],
        help="Type is used to separate Leads and Opportunities")
    