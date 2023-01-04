# -*- coding: utf-8 -*-
from odoo import models, fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "Real estate advertisement module tags"

    name = fields.Char('Name',required=True)

    _sql_constraints = [
        ('tag_name_unique', 'unique(name)', 'Tag name must be unique.'),
    ]

