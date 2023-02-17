from odoo import fields,models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Properties"

    name = fields.Char(required=True)

    #A property tag name must be unique
    _sql_constraints = [
        ('property_tag', 'unique(name)', 'Property Tag Is Already Available.')
    ]