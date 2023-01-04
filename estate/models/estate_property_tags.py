# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateModel(models.Model):
    _name = "estate.property.tags"
    _description = "Estate Property Tags Model"

    name = fields.Char('Name',required = True)

    _sql_constraints = [
        ('unique_property_tags_name', 'unique(name)',
         'The property tags name should be unique')
    ]
