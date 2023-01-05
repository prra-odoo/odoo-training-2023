# -*- coding: utf-8 -*-

from odoo import models , fields

class estate_property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    _order  = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]   
    
    name = fields.Char(required=True)
    description = fields.Char()
    sequence = fields.Integer("Sequence",default = 10)
    title= fields.Char()
    propertyName_id = fields.One2many('estate.property','property_type_id')
    
    