from odoo import fields, models


class RealEstatePropertyType(models.Model):
    _name = "real.estate.property.type"
    _description = "Property Type"

    name = fields.Char(string="Property Type", required=True)
    active = fields.Boolean(default=True)
