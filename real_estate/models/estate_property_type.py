# -*- coding: utf-8 -*-

from odoo import fields,models
class Estate_Property_Type(models.Model):
    _name='estate.property.type'
    _description="Type of Properties"
    _order="name"

    sequence=fields.Integer("sequence",default="1")
    name=fields.Char(required=True)
    property_ids=fields.One2many("real.estate.properties","property_type_id",readonly=True)

    _sql_constraints=[
        ('unique_type','UNIQUE(name)','The type you are trying to create is already exist')
    ]

    

    
