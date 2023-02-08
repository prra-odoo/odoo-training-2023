from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag field"

    name = fields.Char(required=True)