# -- coding: utf-8 --
from odoo import models, fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "estate property tags Model"
    
    name = fields.Char(required=True)   

    _sql_constraints = [
        ('property_tag_unique',
        'unique(name)',
        'The Tag must be unique!!')
    ]