# -*- coding: utf-8 -*-
from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description = "Estate Property Tag Model _description"
    _sql_constraints = [
        ('unique_name','UNIQUE(name)','Tag Name must be unique')
    ]
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()