from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate property type model"

    name = fields.Char(required = True)

    _sql_constraints = [
        ("unique_name","UNIQUE(name)","Tag names must be unique!")
    ]