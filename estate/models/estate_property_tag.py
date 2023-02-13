from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "It's a Estate Property Tag"

    name = fields.Char(required=True)