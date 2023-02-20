# -*- coding: utf-8 -*-

from odoo import fields,models,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is Estate Property Type Model"
    _order = "sequence, name"
    # Table Fields
    name = fields.Char(required=True)
    sequence = fields.Integer(string="Sequence",default=1)
    property_type_ids = fields.One2many('estate.property','property_type_id')
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer(compute="_compute_offer_count",string="Offers")
    # SQL constraints
    _sql_constraints = [
        ('unique_property_type','UNIQUE(name)',"Property Type must have an unique name!")
    ]

    # Compute Offer Count
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
            
        