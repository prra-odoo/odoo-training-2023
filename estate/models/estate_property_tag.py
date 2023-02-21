# -*- coding: utf-8 -*-
from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"
    _order = "name"

    name = fields.Char(required=True)
    colors = fields.Integer()

    _sql_constraints = [
        ('check_tag_name','unique(name)','The property tag name must be unique.')
    ]
