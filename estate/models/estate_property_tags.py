from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Real-estate property tags"

    name = fields.Char(required=True)