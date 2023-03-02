# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag Model"
    _order = "sequence"

    name = fields.Char(required=True)
    color_tag = fields.Integer()
    sequence = fields.Integer('sequence')
    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'This Property type alredy added.')
    ]
