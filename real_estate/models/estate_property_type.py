# -*- coding: utf-8 -*-

from odoo import fields,models

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Real Estate Type Model"

    name = fields.Char(string='Name')

