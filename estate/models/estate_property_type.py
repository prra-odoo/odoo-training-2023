# -*- coding: utf-8 -*-

from odoo import models,fields

class estatePropertyType(models.Model):
    _name ="estate.property.type"
    _description="This model defines the property type for Estate Property Module"

    name = fields.Char(required=True)
    property_list_ids=fields.One2many('estate.property','property_type_id',string="Property List")

    _sql_constraints=[('property_type_unique','unique(name)','!!This property type is already there.')]
    


