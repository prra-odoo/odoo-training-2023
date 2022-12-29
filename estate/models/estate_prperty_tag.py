# -*- coding: utf-8 -*-

from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.tag"
    _description = "Tags of the different Real Estate Property"

    name = fields.Char(required = True)