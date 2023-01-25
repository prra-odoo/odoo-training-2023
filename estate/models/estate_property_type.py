# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"
    _order = "name"

    name = fields.Char(string ="Name", required =True)
    property_under_type_ids = fields.One2many("estate.property", "property_type_id", string="Properties according to type ")

    _sql_constraints = [
        ('unique_propetytype', 'UNIQUE(name)',
         'The Type should be Unique')
    ]

