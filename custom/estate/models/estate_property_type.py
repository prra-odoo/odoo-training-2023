from odoo import models,fields
class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Property Type must be unique'),
    ]


    name=fields.Char()
    

