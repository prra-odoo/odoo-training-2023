# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real estate advertisement module types"
    _order = "sequence, name"

    name = fields.Char('Name',required=True)

    property_ids = fields.One2many('estate.property', 'property_type_id', string="Property Name")
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer('Offer count', compute="_compute_count")

    sequence = fields.Integer('Sequence')
    _sql_constraints = [
        ('property_type_unique', 'unique(name)', 'Property type already exist!'),
    ]

    @api.depends('offer_ids','offer_count')
    def _compute_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)