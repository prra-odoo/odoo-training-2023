# -*- coding: utf-8 -*-

from odoo import models , fields,api

class estate_property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    _order  = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]   
    
    name = fields.Char(required=True)
    description = fields.Char()
    sequence = fields.Integer()
    title= fields.Char()
    propertyName_ids = fields.One2many('estate.property','property_type_id')
    offer_count = fields.Integer('Property type count',compute="_compute_offer_")
    offer_ids = fields.One2many("estate.property.offer","property_type_id",string = "Offers")
    
    @api.depends('offer_ids')
    def _compute_offer_(self):
        for record in self:
            record.offer_count = len(record.offer_ids)        
    
    
    
    
    