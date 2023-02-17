from odoo import models,fields,_

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "New Estate Propert Type Module "

    name = fields.Char(required=True)

    _sql_constraints=[(
        'property_type_unique',
        'unique(name)',
        'Property Type must be Unique.'
    )]