from odoo import fields,models

class Property_type(models.Model):
    _name = "estate.property.type"
    _description = "Estate property types"
    _order = "name"

    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence')
    property_ids = fields.One2many("estate.property.model","type_id",readonly=True)

    _sql_constraints = [
        ('unique_type_name','unique(name)','Type name must be unique'),
    ]
    