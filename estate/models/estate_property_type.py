# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of the different Real Estate Property"
    _order = "name"

    name = fields.Char(required=True)
    property_name_ids = fields.One2many(
        "estate.property", 'property_type_id', string="Property Name")
    sequence = fields.Integer("Sequence")

    _sql_constraints = [
        ("unique_property_type", "unique(name)","Property Types can't Be Same")
    ]
