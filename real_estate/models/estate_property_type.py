# -*- coding: utf-8 -*-

from odoo import models, fields 

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A property type is, for example, a House or an Apartment."
    
    name = fields.Char(string="Type", required=True)