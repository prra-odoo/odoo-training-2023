# -*- coding: utf-8 -*-
from odoo import fields, models

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Estate Property Type Model _description"
    _sql_constraints = [
        ('name','UNIQUE(name)','Type Name must be unique')
    ]
    _order = "sequence,name asc"
    

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property","property_type_id",string="Properties")
    sequence = fields.Integer("Sequence",default=1)