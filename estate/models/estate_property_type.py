# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstateModel(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "sequence, name"

    name = fields.Char('Name',required = True)
    list_property = fields.One2many("estate.property", "property_type_id")
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Offers")
    offer_count = fields.Integer(compute="_compute_offer_count")

    _sql_constraints = [
        ('unique_property_type_name', 'unique(name)',
         'The property type name should be unique')
    ]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
