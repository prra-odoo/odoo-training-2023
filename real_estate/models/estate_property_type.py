# -*- coding: utf-8 -*-

from odoo import models, fields

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Regarding Real Estate Properties Type"
    _order = "name"

    name = fields.Char(required=True)
    property_type_name_list = fields.One2many('estate.property', 'property_type_id', string="Property Name")
    sequence = fields.Integer('Sequence', default=1)
    _sql_constraints = [
        ('unique_type', 'unique(name)', 'Property Types must be Unique!')
    ]

# class estatePropertyTypeLine(models.Model):
#     _name = "estate.property.type.line"
#     _description = "Estate Property Type Line"

#     model_id = fields.Many2one("estate.property.type")