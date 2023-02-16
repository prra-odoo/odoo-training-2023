from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Properties"

    name = fields.Char(required=True)

_sql_constraints = [
     ('property_type', 'unique(name)', 'This property type is already available.')
]