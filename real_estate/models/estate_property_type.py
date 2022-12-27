# -*- coding: utf-8 -*-

from odoo import models,fields

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Real Estate Type Model"

    name = fields.Char('Name')

