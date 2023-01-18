from odoo import models,fields

class estate_Property_buyer(models.Model):
      _name = "estate.property.buyer"
      _description = "Real estate based advertisedment module for the property type"
      
      name=fields.Char()