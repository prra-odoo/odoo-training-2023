# -*- coding: utf-8 -*-

from odoo import fields,models

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Real Estate Type Model"
    _order = "name desc"

    name = fields.Char(string='Name')
    property_ids=fields.One2many("estate.property", "property_type_id")
    sequence=fields.Integer(string='Sequence', default=1)

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'A Property type name should be unique.'),
    ]
