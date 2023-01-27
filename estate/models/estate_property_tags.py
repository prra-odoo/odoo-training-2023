# -*- coding: utf-8 -*-

from odoo import fields, models
from random import randint


class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "estate property tags model"
    _order = "name"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string ="Name", required =True)
    color = fields.Integer(string='Color', default=_get_default_color)


    _sql_constraints = [
        ('unique_tags', 'UNIQUE(name)',
         'The Tags should be Unique')
    ]