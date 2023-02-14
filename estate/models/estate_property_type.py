from odoo import models,fields

class EstatePropertyType(models.Model):
    
    _name = "estate.property.type"
    _description = "Property Type Model"

    name = fields.Char(required=True)
    _sql_constraints = [
          ('name_uniq', 'unique (name)', "Property type already exists !"),
       ]
