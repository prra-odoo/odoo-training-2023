from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Model for property tags"
    _order = "name"

    name = fields.Char(required = True)
    color = fields.Integer()

    _sql_constraints = [
        ("unique_name","UNIQUE(name)","Tag names must be unique!")
    ]