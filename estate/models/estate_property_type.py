# -- coding: utf-8 --
from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type Model"
    _order = "sequence,name asc"
    
    name = fields.Char(required=True)   
    property_ids = fields.One2many("estate.property", "property_type_id")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    _sql_constraints = [
        ('property_type_unique',
        'unique(name)',
        'The Property Type must be unique!!')
    ]
