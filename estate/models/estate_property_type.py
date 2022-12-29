# -*- coding: utf-8 -*-

from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of the different Real Estate Property"

    name = fields.Char(required = True)

