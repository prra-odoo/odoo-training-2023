# -*- coding: utf-8 -*-

from odoo import models , fields

class estate_propertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    
    name = fields.Char(required=True)

    
    
    