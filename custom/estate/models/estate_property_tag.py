from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _sql_constraints = [
        ('uniq_tag', 'unique(name)', 'Property Tag must be unique'),
    ]
    name = fields.Char()
