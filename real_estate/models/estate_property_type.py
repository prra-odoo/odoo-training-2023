# -*- coding: utf-8 -*-

from odoo import models, fields, api

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Regarding Real Estate Properties Type"
    _order = "name"

    name = fields.Char(required=True)
    property_type_name_list = fields.One2many('estate.property', 'property_type_id', string="Property Name")
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    offer_count = fields.Integer(compute="_compute_offer_count", string="Offer Count")

    _sql_constraints = [
        ('unique_type', 'unique(name)', 'Property Types must be Unique!')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    # def action_offers(self):
    #     return
