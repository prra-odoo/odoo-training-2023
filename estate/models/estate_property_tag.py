# -*- coding: utf-8 -*-
from odoo import models,fields

class Estate_Property_Tag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"
    _sql_constraints = [
        ("unique_property_type_name", "UNIQUE(name)","The property type name must be unique"),
    ]

    name = fields.Char(string = 'name',required=True)