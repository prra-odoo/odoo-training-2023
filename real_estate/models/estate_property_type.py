# -*- coding:utf:8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Type module"
    _order = "name desc"

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer('Sequence')
    offer_count = fields.Integer('Offer count', compute="_compute_offer_count")
    active = fields.Boolean(default=True)

    offeres_ids = fields.One2many(
        "estate.property.offer", "property_type_id", string="Offer IDs")
    offer_ids = fields.One2many(
        "estate.property", "property_type_id", string="Offer")
    
    
    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'Name must be unique')
    ]

    @api.depends('offeres_ids', 'offer_count')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offeres_ids)
