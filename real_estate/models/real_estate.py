#-*- coding:utf:8 -*- 

from odoo import models,fields,api

class RealEstateAd  (models.Model): 
     _name = "estate.property"
     # real.estate
     _description = "Real Estate Advertisement module" 

     name = fields.Char(string='Name') 
     description = fields.Text(string='Description')
     postcode =fields.Char(string='Postcode')
     date_availability=fields.Date(string='Date Available',default=lambda self: fields.Datetime.now())
     expected_price = fields.Float(string='Price')
     selling_price = fields.Float(string='Selling Price')
     bedrooms =fields.Integer(string='Bedrooms')
     living_area=fields.Integer(string='Living Area')
     facades=fields.Integer(string='Facades')
     garage=fields.Boolean(string='Garage')  
     garden=fields.Boolean(string='Garden')
     
     garden_area =fields.Integer(string='Garden Area')
     garden_orientation =fields.Selection(
          string='Garden Orientation',
          selection=[('south','South'),('west', 'West'),('north','North'),('east', 'East')]   
          )
     state =fields.Selection(
          selection=[('new','New'),('confirm', 'Confirm'),('cancel','Cancel')],default="new"   
          )     
     property_buyer_id = fields.Many2one("res.partner", string="Buyer")
     property_seller_id = fields.Many2one("res.users", string="Salesman",default=lambda self: self.env.user)
     property_type_id = fields.Many2one("estate.property.type", string="Property Type")
     tag_ids = fields.Many2many("estate.property.tag", string="Tag")
     #estate_property_offer
     offer_ids = fields.One2many('estate.property.offer','property_id')
     # status= fields.One2many('estate.property.offer')
     # partner_id=fields.One2many('estate.property.offer')

     # Api depends
     
