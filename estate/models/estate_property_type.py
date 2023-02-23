from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is a PropertyType model"
    _order = "name"

    _sql_constraints = [("type_uniq", "UNIQUE (name)",
                         "The type must be different from already defined types."),
                        ("type_notnull", "CHECK (name IS NOT NULL)",
                         "Property type cannot be NULL"),]

    name = fields.Char(string="Property Type")

    property_ids = fields.One2many(
        comodel_name="estate.property", inverse_name="property_type_id")

    sequence = fields.Integer(
        default=1, help="Used to order stages.", string="Sequence")
