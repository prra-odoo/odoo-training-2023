# -*- coding: utf-8 -*-
from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real estate advertisement module types"
    _order = "sequence, name"

    name = fields.Char('Name',required=True)

    property_ids = fields.One2many('estate.property', 'property_type_id', string="Property Name")

    sequence = fields.Integer('Sequence', default=1, help='order property types')
    _sql_constraints = [
        ('property_type_unique', 'unique (name)', 'Property type already exist!'),
    ]