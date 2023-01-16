# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate property types"
    _order="name"

    name=fields.Char('Name',required=True)
    sequence=fields.Integer('Sequence',default=1)
    active=fields.Boolean('Active',default=True)
    property_ids=fields.One2many('estate.properties','type_id', string="properties:",readonly=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A property type with the same name already exists."),
    ]