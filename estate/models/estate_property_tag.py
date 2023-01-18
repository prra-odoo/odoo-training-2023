# -*- coding: utf-8 -*-
from odoo import fields,models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is Estate property tags model"
    # Table Fields
    name = fields.Char(required=True)