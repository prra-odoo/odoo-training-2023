# -*- coding: utf-8 -*-
from odoo import models,fields,api

class estate_Property_type(models.Model):
      _name = "estate.property.type"
      _description = "Real estate based advertisedment module for the property type"
      _order="name"
      
      name = fields.Char(required=True)
      sales_id = fields.Many2one('estate.property.sales', string='Salesperson')
      buyer_id=fields.Many2one('estate.property.buyer', string='buyer')
      offer_ids = fields.One2many('estate.property.offer','property_type_id')
      property_ids=fields.One2many('estate.property','type_id')
      sequence=fields.Integer()
      offer_count=fields.Integer(compute='_computed_offer_count')
        
      @api.depends('offer_ids','offer_ids')
      def _computed_offer_count(self):
        for record in self:
          record.offer_count=len(record.offer_ids)

