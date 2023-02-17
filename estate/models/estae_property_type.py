# -*- coding: utf-8 -*-
from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('check_property_type','unique(name)','The property type name must be unique.')
    ]
