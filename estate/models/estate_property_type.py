# -*- coding: utf-8 -*-

from odoo import fields, models, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"
    _order = "name"

    name = fields.Char(string ="Name", required =True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    property_under_type_ids = fields.One2many("estate.property", "property_type_id", string="Properties according to type ")
    offer_ids = fields.One2many(related="property_under_type_ids.offer_ids")
    offer_count=fields.Integer(compute="_compute_offer_count")

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for records in self.offer_ids:
            self.offer_count+=1 

    _sql_constraints = [
        ('unique_propetytype', 'UNIQUE(name)',
         'The Type should be Unique')
    ]

