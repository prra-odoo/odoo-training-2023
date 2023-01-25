# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "estate property tags model"
    _order = "name"

    name = fields.Char(string ="Name", required =True)

    _sql_constraints = [
        ('unique_tags', 'UNIQUE(name)',
         'The Tags should be Unique')
    ]