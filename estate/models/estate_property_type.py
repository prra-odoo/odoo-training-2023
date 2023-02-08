from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is a PropertyType model"

    name = fields.Char(required=True)
