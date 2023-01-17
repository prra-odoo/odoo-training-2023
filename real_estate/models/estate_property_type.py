# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,models,fields

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate property types"
    _order="name"

    name=fields.Char('Name',required=True)
    sequence=fields.Integer('Sequence',default=1)
    active=fields.Boolean('Active',default=True)
    property_ids=fields.One2many('estate.properties','type_id', string="properties:",readonly=True)
    offer_ids=fields.One2many('estate.property.offer','property_type_id')
    offer_count=fields.Integer(compute="_compute_offer_count")

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count=len(record.offer_ids)
            
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A property type with the same name already exists."),
    ]