from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Real-estate property tags"
    _order="name"
    
    name = fields.Char(required=True)
    color=fields.Integer('Colour Index',default=0)

    _sql_constraints=[(
        'name_unique',
        'unique(name)',
        'Tag name already exists'
    )]