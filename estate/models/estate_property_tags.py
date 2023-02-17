from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Real-estate property tags"

    name = fields.Char(required=True)

    _sql_constraints=[(
        'name_unique',
        'unique(name)',
        'Tag name already exists'
    )]