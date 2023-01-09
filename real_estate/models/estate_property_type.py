# -*- coding: utf-8 -*-

from odoo import fields,models
class Estate_Property_Type(models.Model):
    _name='estate.property.type'
    _description="Type of Properties"

    name=fields.Char(required=True)
    
