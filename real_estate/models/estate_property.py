# -*- coding: utf-8 -*-
from odoo import fields,models

class estatePropertyType(models.Model):
     _name = "estate.property.type"
     _description = "This is regarding the real_estate"
     _order = "name"

     name = fields.Char(string='Name',required = True)
     details=fields.One2many('real.estate','property_type_id')
     sequence = fields.Integer('Sequence', default=1)
     
     _sql_constraints = [
          ('name_unique','UNIQUE(name)','Name must be unique!!')
     ]