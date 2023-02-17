# -*- coding: utf-8 -*-
from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('check_tag_name','unique(name)','The property tag name must be unique.')
    ]
