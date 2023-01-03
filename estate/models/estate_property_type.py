# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateModel(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char('Name',required = True)
    list_property = fields.One2many("estate.property", "property_type_id")
