# -*- coding: utf-8 -*-
from odoo import fields,models

class estatePropertyType(models.Model):
     _name = "estate.property.type"
     _description = "This is regarding the real_estate"

     name = fields.Char(string='Name',required = True)
     details=fields.One2many('real.estate','property_type_id')
     
     _sql_constraints = [
          ('name_unique','UNIQUE(name)','Name must be unique!!')
     ]