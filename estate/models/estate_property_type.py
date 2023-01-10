# -*- coding: utf-8 -*-

from odoo import models, fields,api

class estatepropertytype(models.Model):
    _name = "estate.property.type"
    _description="Property types module"
    _order = "name desc"

    name = fields.Char(string="Name",required=True)
    propertyname = fields.One2many("estate.property","property_type_id",string="Present Properties")
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer(compute="_compute_offer_count")

    _sql_constraints = [
        ('checktype', 'unique (name)', "Property name cannot be similar"),
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        self.offer_count = len(self.offer_ids)
        print(self.offer_count)
