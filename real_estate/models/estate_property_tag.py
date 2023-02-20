# -*- coding: utf-8 -*-
from odoo import fields, models


class estatePropertytag(models.Model):
    _name = "estate.property.tag"
    _description = "This is regarding the real_estate"
    _order = "name"

    name = fields.Char(string='Name', required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Name must be unique!!')
    ]
