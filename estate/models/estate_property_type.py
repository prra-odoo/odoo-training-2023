# -*- coding: utf-8 -*-

from odoo import models , fields

class estate_property(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    
    name = fields.Char(required=True)
    
    
    