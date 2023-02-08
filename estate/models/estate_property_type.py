from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type field"

    name = fields.Char(required=True)