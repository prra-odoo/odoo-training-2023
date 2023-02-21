from odoo import models,fields,_

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "New Estate Propert Type Module "
    _order="sequence,name"

    name = fields.Char(required=True)
    property_ids =fields.One2many('estate.property','property_type_ID')
    sequence=fields.Integer('Sequence',default=1,help="sequence_manually")
    _sql_constraints=[(
        'property_type_unique',
        'unique(name)',
        'Property Type must be Unique.'
    )]

