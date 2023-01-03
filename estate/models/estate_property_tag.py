# -*- coding: utf-8 -*-

from odoo import models, fields

class estateTag(models.Model):
    _name = "estate.property.tag"
    _description = "This module of estate property tag"
    
    name = fields.Char(required=True)
