# -*- coding: utf-8 -*-

from odoo import fields,models

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"

    name = fields.Char(string='Name',required=True)

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'A Property tag name should be unique.'),
    ]
    