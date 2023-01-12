# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate property types"

    name=fields.Char('Name',required=True)
    active=fields.Boolean('Active')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A property type with the same name already exists."),
    ]