# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A property type is, for example, a House or an Apartment."
    _order = "sequence, name"
    
    name = fields.Char(string="Type", required=True)
    sequence = fields.Integer(string="Sequence", default=1, help="Used to order property types.")
    property_ids = fields.One2many('estate.property', 'property_type_id')
    offer_ids = fields.One2many('estate.property.offer', "property_type_id", string="Offer IDs")
    offer_count = fields.Integer(string="Offer Count", compute="_compute_offers_count")
    
    _sql_constraints = [('type_name_unique', 'unique (name)', "A type with the same name already exists.")]
    
    @api.depends("offer_count", "offer_ids")
    def _compute_offers_count(self):
        for record in self:    
            record.offer_count = len(record.offer_ids)
        return True