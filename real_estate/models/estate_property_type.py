# -*- coding: utf-8 -*-
from odoo import models,fields,api

class estate_property_type(models.Model):
    _name = 'estate.property.type'
    _description = "Estate Property Type"
    _order = "name"

    name = fields.Char("Property type",required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many('estate.property.offer','property_type_id',string='property type offer')
    offer_count = fields.Integer('offer count',compute='_offer_count',default=0)

    @api.depends('offer_ids','offer_count')
    def _offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
