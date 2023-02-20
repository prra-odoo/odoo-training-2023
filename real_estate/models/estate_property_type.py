from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Properties"
    _order="sequence,name,id"

    name = fields.Char(required=True)

    #property type name must be unique
    _sql_constraints = [
        ('property_type', 'unique(name)', 'Property Type Is Already Available.')
    ]

    property_ids = fields.One2many("estate.property", "property_type_id")
    sequence = fields.Integer('Sequence', default=1)


   

