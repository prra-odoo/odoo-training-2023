# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "sequence, name"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer(default=1, help="Used to order property type.")
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer(compute='_compute_offer_count', default=0)
    _sql_constraints = [
        ('check_property_type','unique(name)','The property type name must be unique.')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
