# -*- coding: utf-8 -*-

from odoo import models, fields,api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of the different Real Estate Property"
    _order = "name"

    name = fields.Char(required=True)
    property_name_ids = fields.One2many(
        "estate.property", 'property_type_id', string="Property Name")
    sequence = fields.Integer("Sequence")
    offer_ids = fields.One2many('estate.property.offer','property_type_id',string="Offers")
    offer_count = fields.Integer(compute="_offer_count",string="Offer Count")


    _sql_constraints = [
        ("unique_property_type", "unique(name)","Property Types can't Be Same")
    ]

    @api.depends("offer_ids")
    def _offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)