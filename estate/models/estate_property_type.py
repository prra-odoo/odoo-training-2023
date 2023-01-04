# -*- coding: utf-8 -*-

from odoo import models , fields

class estate_property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]
    
    name = fields.Char(required=True)
    # description_id = fields.Many2one("estate.property.offer",string="Property_id")
    # # property_id= fields.Many2one("estate.property",string="Property id")
    
    
    