from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is a PropertyType model"

    _sql_constraints = [("type_uniq", "UNIQUE (name)",
                         "The type must be different from already defined types."),
                        ("type_notnull", "CHECK (name IS NOT NULL)",
                         "Property type cannot be NULL"),]

    name = fields.Char(string="Property Type")
