# -*- coding: utf-8 -*-
from odoo import fields, models

class estate_property_tag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag model"
    _sql_constraints = [
        ("unique_tag_names", "UNIQUE(name)", "A property tag name must be unique"),
    ]


    name=fields.Char(string="Name",required=True)