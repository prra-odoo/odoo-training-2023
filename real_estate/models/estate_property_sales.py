from odoo import models,fields

class estate_Property_sales(models.Model):
      _name = "estate.property.sales"
      _description = "Real estate based advertisedment module for the property type"

      
      name=fields.Char()