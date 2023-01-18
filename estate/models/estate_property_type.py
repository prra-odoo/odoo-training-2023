# -*- coding: utf-8 -*-

from odoo import fields, models


class estate_property_type(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"

    name = fields.Char(string ="Name", required =True)
    property_under_type_ids = fields.One2many("estate.property", "property_type_id", string="Properties according to type ")
