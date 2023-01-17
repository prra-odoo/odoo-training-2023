# -*- coding: utf-8 -*-

from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "A property tag is, for example, a property which is Cozy or Renovated."
    _order = "name"
    
    name = fields.Char(string="Tags", required=True)
    color = fields.Integer(string="Color Index", default=0)
    
    _sql_constraints = [('tag_name_unique', 'unique (name)', "A tag with the same name already exists.")]