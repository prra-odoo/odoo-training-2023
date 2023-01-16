# -*- coding: utf-8 -*-
from odoo import models,fields

class estate_Property_type(models.Model):
      _name = "estate.property.type"
      _description = "Real estate based advertisedment module for the property type"
      _order="name"
      
      name = fields.Char(required=True)
      sales_id = fields.Many2one('estate.property.sales', string='Salesperson')
      buyer_id=fields.Many2one('estate.property.buyer', string='buyer')
      property_ids=fields.One2many('estate.property','type_id')
      sequence=fields.Integer()
      # name=fields.Char()
      # expeccted_price=fields.Integer()
      