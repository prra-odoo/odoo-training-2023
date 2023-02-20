from odoo import fields,models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Properties"
    _order="name desc"

    name = fields.Char(required=True)
    color=fields.Integer()

    #A property tag name must be unique
    _sql_constraints = [
        ('property_tag', 'unique(name)', 'Property Tag Is Already Available.')
    ]