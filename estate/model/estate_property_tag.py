# -*- coding: utf-8 -*-
from odoo import models, fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "Real estate advertisement module tags"
    _order = "sequence, name"

    name = fields.Char('Name',required=True)
    color = fields.Integer('Color')
    sequence = fields.Integer('Sequence')
    propertys_ids = fields.Many2many("estate.property", string="Properties") #relation table --> estate_property_estate_property_tag_rel


    _sql_constraints = [
        ('tag_name_unique', 'unique(name)', 'Tag name must be unique.'),
    ]


