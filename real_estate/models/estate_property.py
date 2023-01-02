# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate module properties"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date()
    expected_price = fields.Float(string="Expected Price", required=True, help='What is your expected price of the property?')
    selling_price = fields.Float(string="Selling Price", required=True, help='What is your selling price of the property?')
    bedrooms = fields.Integer(string="Bedrooms", help="No. of Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)", help="How much Area does your Living Room contain?")
    facades = fields.Integer(string='Facades', help="The Facade is the front of the Property that is usually seen from the outside.")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)", help="How much Area does your Garden contain?")
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
