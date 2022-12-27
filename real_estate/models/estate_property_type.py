#-*- coding:utf:8 -*- 

from odoo import models,fields 

class estatePropertyType  (models.Model): 
     _name = "estate.property.type"
     # real.estate
     _description = "estate property type" 

     name = fields.Char(string='Name') 