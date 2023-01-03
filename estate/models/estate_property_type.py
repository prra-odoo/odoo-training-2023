# -*- coding: utf-8 -*-

from odoo import models , fields

class estate_property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    
    name = fields.Char(required=True)
    property_id= fields.Many2one("estate.property",string="Property id")
    
    
    