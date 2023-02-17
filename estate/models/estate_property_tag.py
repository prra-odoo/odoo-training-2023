from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Model for property tags"

    name = fields.Char(required = True)

    _sql_constraints = [
        ("unique_name","UNIQUE(name)","Tag names must be unique!")
    ]
