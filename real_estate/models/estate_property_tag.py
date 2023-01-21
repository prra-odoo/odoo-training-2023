# -*- coding: utf-8 -*-

from odoo import models, fields

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Consists Property Tags"
    _order = "name"

    # Fields
    name = fields.Char(required=True)
    Color = fields.Integer()
    
    # SQL Constraints
    _sql_constraints = [
        ('unique_tag', 'unique(name)', 'Tag name must be Unique!')
    ]
