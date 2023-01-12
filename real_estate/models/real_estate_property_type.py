from odoo import fields, models


class RealEstatePropertyType(models.Model):
    _name = "real.estate.property.type"
    _description = "Property Type"

    name = fields.Char(string="Property Type", required=True)
    active = fields.Boolean(default=True)
    property_ids = fields.One2many("real.estate.property", "property_type_id", string="Offers")

    _sql_constraints = [('unique_type_name', 'UNIQUE(name)','The Name of an property type must be unique.')]
