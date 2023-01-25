# -*- coding: utf-8 -*-

from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is Estate Property Type Model"
    _order = "name"
    # Table Fields
    name = fields.Char(required=True)
    property_type_ids = fields.One2many('estate.property','property_type_id')

    _sql_constraints = [
        ('unique_property_type','UNIQUE(name)',"Property Type must have an unique name!")
    ]