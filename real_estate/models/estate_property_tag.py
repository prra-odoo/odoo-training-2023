# -*- coding: utf-8 -*-

from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "A property tag is, for example, a property which is Cozy or Renovated."
    
    name = fields.Char(string="Tags", required=True)