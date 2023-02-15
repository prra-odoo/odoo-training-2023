# -*- coding: utf-8 -*-
from odoo import fields, models

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Estate Property Type Model _description"
    _sql_constraints = [
        ('name','UNIQUE(name)','Type Name must be unique')
    ]

    name = fields.Char(required=True)