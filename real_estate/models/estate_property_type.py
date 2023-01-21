# -*- coding: utf-8 -*-

from odoo import models, fields, api

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Regarding Real Estate Properties Type"
    _order = "name"

    # Fields
    name = fields.Char(required=True)
    sequence = fields.Integer(default=1)
    
    # Relational Fields
    property_type_name_list = fields.One2many('estate.property', 'property_type_id', string="Property Name")
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    
    # Computed Fields
    offer_count = fields.Integer(compute="_compute_offer_count", string="Offer Count")

    # SQL Constraints
    _sql_constraints = [
        ('unique_type', 'unique(name)', 'Property Types must be Unique!')
    ]

    # Compute Methods
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
