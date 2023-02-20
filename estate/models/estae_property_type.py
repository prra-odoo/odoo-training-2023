# -*- coding: utf-8 -*-
from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "sequence, name"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    # sequence = fields.Integer(default=1, help="Used to order stages.")

    _sql_constraints = [
        ('check_property_type','unique(name)','The property type name must be unique.')
    ]
