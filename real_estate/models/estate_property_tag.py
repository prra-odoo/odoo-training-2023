#-*- coding:utf:8 -*- 

from odoo import models,fields  

class estatePropertyTag  (models.Model): 
     _name = "estate.property.tag"
     # real.estate
     _description = "Real Estate tag module" 


     t_name=fields.Char()
     description = fields.Text(string='Description')