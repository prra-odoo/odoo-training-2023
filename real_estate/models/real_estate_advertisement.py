#-*- coding:utf:8 -*- 

from odoo import models,fields  

class RealEstateAd  (models.Model): 
     _name = "real.estate"
     _description = "Real Estate Advertisement module" 

     name = fields.Char(string='Name',required=True) 
     description = fields.Text(string='Description')
     postcode =fields.Char(string='Postcode',required=True)
     date_availability=fields.Date(string='Date Available',required=True)
     expected_price = fields.Float(string='Price',required=True)
     selling_price = fields.Float(string='Selling Price',required=True)
     bedrooms =fields.Integer(string='Bedrooms')
     living_area=fields.Integer(string='Living Area')
     facades=fields.Integer(string='Facades')
     garage=fields.Boolean(string='Garage')
     garden=fields.Boolean(string='Garden',required=True)
     garden_area =fields.Integer(string='Garden Area')
     garden_orientation =fields.Selection(
          string='Type',
          selection=[('south','South'),('west', 'West'),('north','North'),('east', 'East')],
         
     )
