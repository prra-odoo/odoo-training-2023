# -*- coding: utf-8 -*-
from odoo import fields,models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is Estate property tags model"
    _order = "name"
    # Table Fields
    name = fields.Char(required=True)

    _sql_constraints = [
        ('unique_tag_name','unique(name)','Property Tag name should be unique!')
    ]