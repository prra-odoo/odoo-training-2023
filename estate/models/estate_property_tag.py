from odoo import models,fields

class EstatePropertyTag(models.Model):
    
    _name = "estate.property.tag"
    _description = "Property Tag Model"

    name = fields.Char(required=True)
    _sql_constraints = [
          ('name_uniq', 'unique (name)', "Property tag already exists !"),
       ]