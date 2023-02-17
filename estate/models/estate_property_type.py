# -- coding: utf-8 --
from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type Model"
    
    name = fields.Char(required=True)   

    _sql_constraints = [
        ('property_type_unique',
        'unique(name)',
        'The Property Type must be unique!!')
    ]