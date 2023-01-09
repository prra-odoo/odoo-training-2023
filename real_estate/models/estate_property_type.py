# -*- coding: utf-8 -*-
from odoo import fields,models

class estatePropertyType(models.Model):
     _name = "estate.property.type"
     _description = "This is regarding the real_estate"
     _order = "name"

     name = fields.Char(string='Name',required = True)
     details=fields.One2many('real.estate','property_type_id')
     sequence = fields.Integer('Sequence', default=1)
     offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Estate Offer")
     offer_count = fields.Integer(string="offer count",compute="_compute_offer")
     _sql_constraints = [
          ('name_unique','UNIQUE(name)','Name must be unique!!')
     ]
     
     def _compute_offer(self):
          for record in self:
               record.offer_count =len(record.offer_ids)