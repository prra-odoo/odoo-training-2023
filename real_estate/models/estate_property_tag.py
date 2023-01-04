# -*- coding:utf:8 -*-

from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Tag module"
    _order = "name desc"

    name = fields.Char(required=True)
    color = fields.Integer(string="color")


    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'Name must be unique')
    ]