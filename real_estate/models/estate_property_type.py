# -*- coding: utf-8 -*-

from odoo import models, fields

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Regarding Real Estate Properties Type"

    name = fields.Char(required=True)
