# -*- coding: utf-8 -*-
from odoo import models, fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "Real estate advertisement module tags"
    _order = "name"

    name = fields.Char('Name',required=True)
    color = fields.Integer('Color')


    _sql_constraints = [
        ('tag_name_unique', 'unique(name)', 'Tag name must be unique.'),
    ]

