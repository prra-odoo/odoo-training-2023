# -*- coding: utf-8 -*-
from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description = "Estate Property Tag Model _description"

    name = fields.Char(required=True)