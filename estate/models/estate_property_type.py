# -*- coding: utf-8 -*-
from odoo import fields, models,api


class estate_property_type(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"
    _order = "name"
    _sql_constraints = [
        ("unique_property_type", "UNIQUE(name)", "Property Type must be unique"),
    ]

    name=fields.Char(string="Name",required=True)
    property_types_ids=fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer(string="Sequence")
    # ...........................('RELATED MODEL','RELATED FIELD')
    offer_ids = fields.One2many('estate.property.offer','property_offers_id')
    offer_count = fields.Integer( string='Offers', compute='_compute_offer_count')

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count= len(record.offer_ids)
    

    