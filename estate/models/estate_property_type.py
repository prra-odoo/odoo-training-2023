# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Estate Property Type Model _description"
    _sql_constraints = [
        ('unique_name','UNIQUE(name)','Type Name must be unique')
    ]
    _order = "sequence,name"
    

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property","property_type_id",string="Properties")
    sequence = fields.Integer("Sequence",default=1)
    offer_ids = fields.One2many("estate.property.offer","property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            if(record.offer_ids):
                record.offer_count = len(record.offer_ids)
            else:
                record.offer_count = 0
        