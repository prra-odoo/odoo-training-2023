from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real-estate property type"

    name = fields.Char(required=True)   

    _sql_constraints=[(
        'name_unique',
        'unique(name)',
        'Property Type name already exists')
    ]