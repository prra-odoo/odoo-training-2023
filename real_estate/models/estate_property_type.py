# -*- coding: utf-8 -*-

from odoo import models, fields

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Regarding Real Estate Properties Type"

    name = fields.Char(required=True)
    property_type_name_list = fields.One2many('estate.property', 'property_type_id', string="Property Name")
