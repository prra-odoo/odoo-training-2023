from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "It's a Estate Property Tag"
    _order = "name desc"

    name = fields.Char(required=True)
    color = fields.Integer()
    # Sql contrainsts
    _sql_constraints = [
        ("unique_name","UNIQUE(name)","A property tag name must be unique"),
    ]