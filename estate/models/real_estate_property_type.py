from odoo import models, fields


class EstatePropertyTypeModel(models.Model):
    _name = "estate.property.type"
    _description = "this is the Property Type Model"
    _sql_constraints = [
        (
            'unique_property_type',
            'unique (name)',
            'Property Type should be Unique'
        )
    ]

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
