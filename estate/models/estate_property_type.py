from odoo import models,fields,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate property type model"
    _order = "name"

    name = fields.Char(required = True)
    sequence = fields.Integer("Sequence",default=1)
    property_ids = fields.One2many("estate.property","property_type_id")

    _sql_constraints = [
        ("unique_name","UNIQUE(name)","Tag names must be unique!")
    ]
