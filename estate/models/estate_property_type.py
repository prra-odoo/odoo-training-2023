# -*- coding: utf-8 -*-

from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is Estate Property Type Model"
    # Table Fields
    name = fields.Char(required=True)
    property_type_ids = fields.One2many('estate.property','property_type_id')