# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Estate_Property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _sql_constraints = [
        ("unique_property_type_name", "UNIQUE(name)","The property type name must be unique"),
    ]
    _order = "name"

    name = fields.Char(string = 'name',required=True)
    property_real_type_ids  = fields.One2many("estate.property","property_type_id")
    sequence = fields.Integer(string='sequence',default=1)

    #stat button
    offer_ids = fields.One2many("estate.property.offer","property_type_id",string="Offer")
    offer_count = fields.Integer(compute="_compute_offers")

    @api.depends('offer_ids')
    def _compute_offers(self):
        for record in self:
            record.offer_count= len(record.offer_ids)
    