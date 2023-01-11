# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateModel(models.Model):
    _name = "estate.property.tags"
    _description = "Estate Property Tags Model"
    _order = "name"

    name = fields.Char('Name',required = True)
    color = fields.Integer()
    list_properties = fields.One2many('estate.property', 'tags_ids')

    _sql_constraints = [
        ('unique_property_tags_name', 'unique(name)',
         'The property tags name should be unique')
    ]
