# -*- coding: utf-8 -*-
from odoo import fields, models

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Estate Property Type Model _description"

    name = fields.Char(required=True)