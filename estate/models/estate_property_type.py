# -*- coding: utf-8 -*-
from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type Model"
    _order = "sequence,id"

    name = fields.Char(required=True, string='Property Type')
    sequence = fields.Integer('sequence')
