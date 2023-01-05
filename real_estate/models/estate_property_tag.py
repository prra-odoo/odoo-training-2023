# -*- coding: utf-8 -*-

from odoo import fields,models

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"
    _order = "name desc"

    name = fields.Char(string='Name',required=True)
    color=fields.Integer(string='Color')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'A Property tag name should be unique.'),
    ]
    