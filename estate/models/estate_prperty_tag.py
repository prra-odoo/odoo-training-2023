# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.tag"
    _description = "Tags of the different Real Estate Property"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer(string='Color Index')

    _sql_constraints = [
        ('unique_property_tag', 'unique(name)', 'Property Tags can not Be Same')
    ]
