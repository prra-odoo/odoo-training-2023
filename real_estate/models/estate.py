# -*- coding: utf-8 -*-

from odoo import fields,models

class realEstate(models.Model):
     _name = "real.estate"
     _description = "This is regarding the real_estate"

     name = fields.Char(required = True , string='Name')
     description = fields.Text(string='Description')
     postcode = fields.Char(string='Postcode',required=True)
     date_availability = fields.Date(string='Date Available',required=True)
     expected_price = fields.Float(string='Price',required=True)
     selling_price = fields.Float(tring='Selling Price',required=True)
     bedrooms = fields.Integer(string='Bedrooms')
     living_area = fields.Integer(string='Living Area')
     facades = fields.Integer(string='Facades')
     garage = fields.Boolean(string='Garage')
     garden = fields.Boolean(string='Garden',required=True)
     garden_area = fields.Integer(string='Garden Area')
     garden_orientation = fields.Selection(
          selection =[('3BHK', 'Space'), ('House','Type')]
     )
