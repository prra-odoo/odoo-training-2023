# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type Model"
    _order = "sequence,name"

    name = fields.Char(required=True, string='Property Type')
    sequence = fields.Integer('sequence')
    property_id = fields.One2many('estate.property', 'property_type_id')

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'This Property type alredy added.')
    ]

    offers_id = fields.Many2one('estate.property.offer')
    offer_count = fields.Integer(compute="_compute_offer_count")

    @api.depends('offers_id')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = self.env['estate.property.offer'].search_count([('property_type_id.name','=','record.name')])