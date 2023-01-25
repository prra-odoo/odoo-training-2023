# -*- coding: utf-8 -*-
from odoo import fields, models


class estate_property_type(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"
    _sql_constraints = [
        ("unique_expected_price", "UNIQUE(name)", "Property Type must be unique"),
    ]

    name=fields.Char(string="Name",required=True)
    property_types_ids=fields.One2many('estate.property','property_type_id')