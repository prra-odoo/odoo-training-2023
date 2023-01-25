# -*- coding: utf-8 -*-
from odoo import models,fields

class Estate_Property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char(string = 'name',required=True)
    property_real_type_ids  = fields.One2many("estate.property","property_type_id")
    _sql_constraints = [
        ("unique_property_type_name", "UNIQUE(name)","The property type name must be unique"),
    ]