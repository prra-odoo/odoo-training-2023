#-*- coding:utf:8 -*- 

from odoo import models,fields  

class RealEstateAd  (models.Model): 
     _name = "real.estate"
     _description = "Real Estate Advertisement module" 

     name = fields.Char() 
     description = fields.Text()
     postcode =fields.Char()
     date_availability=fields.Date()
     expected_price = fields.Float()
     selling_price = fields.Float()
     bedrooms =fields.Integer()
     living_area=fields.Integer()
     facades=fields.Integer()
     garage=fields.Boolean()
     garden=fields.Boolean()
     garden_area =fields.Integer()
     garden_orientation =fields.Selection(
          string='Type',
          selection=[('south','South'),('west', 'West'),('north','North'),('east', 'East')],
         
     )
