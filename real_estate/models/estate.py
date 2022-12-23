# -*- coding: utf-8 -*-

from odoo import fields,models

class realEstate(models.Model):
     _name = "real.estate"
     _description = "This is regarding the real_estate"

     name = fields.Char(string='Name')
     description = fields.Text(string='Description')
     postcode = fields.Integer(string='Postcode')
     date_availability = fields.Date(string='Date Available', default=lambda self: fields.Datetime.now())
     expected_price = fields.Float(string='Price')
     selling_price = fields.Float(string='Selling Price')
     bedrooms = fields.Integer(string='Bedrooms')
     living_area = fields.Integer(string='Living Area')
     facades = fields.Integer(string='Facades')
     garage = fields.Boolean(string='Garage')
     garden = fields.Boolean(string='Garden')
     garden_area = fields.Integer(string='Garden Area')
     garden_orientation = fields.Selection(
          selection =[('3BHK', 'Space'), ('House','Type')]
     )
