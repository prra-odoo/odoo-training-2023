# -*- coding: utf-8 -*-

from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is Estate Property Type Model"

    name = fields.Char(required=True)