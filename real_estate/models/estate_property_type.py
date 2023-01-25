# -*- coding: utf-8 -*-

from odoo import fields,models,api
class Estate_Property_Type(models.Model):
    _name='estate.property.type'
    _description="Type of Properties"
    _order="name"

    sequence=fields.Integer("sequence",default="1")
    name=fields.Char(required=True)
    property_ids=fields.One2many("real.estate.properties","property_type_id",readonly=True)
    offer_ids=fields.One2many("estate.property.offer","property_type_id")
    offer_count=fields.Integer(compute="_count_offers")
    
    @api.depends("offer_ids")
    def _count_offers(self):
        for record in self:
            record.offer_count=len(record.offer_ids)
    
    _sql_constraints=[
        ('unique_type','UNIQUE(name)','The type you are trying to create is already exist')
    ]

    

    
