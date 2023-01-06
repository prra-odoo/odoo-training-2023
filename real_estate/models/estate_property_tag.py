from odoo import models,fields

class estate_Property_type(models.Model):
      _name = "estate.property.tag"
      _description = "Real estate based advertisedment module for the property tag"

      name = fields.Char(required=True)