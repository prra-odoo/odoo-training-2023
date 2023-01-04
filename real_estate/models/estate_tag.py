from odoo import fields, models
from odoo.exceptions import UserError


class propertytag(models.Model):
    _name="estate.property.tag"
    _description = "property tag model"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    name = fields.Char('Name')

    