# -*- coding: utf-8 -*-

from odoo import fields,models

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Real Estate Type Model"

    name = fields.Char(string='Name')
    details=fields.One2many("estate.property", "property_type_id")

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'A Property type name should be unique.'),
    ]
