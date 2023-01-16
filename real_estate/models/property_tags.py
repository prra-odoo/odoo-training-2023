# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields

class PropertyTags(models.Model):
    _name="estate.property.tags"
    _description="Estate property tags"
    _order="name"

    name=fields.Char('Name', required=True)
    color=fields.Integer('color')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A tag with the same name already exists."),
    ]