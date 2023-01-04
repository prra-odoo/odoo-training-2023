# -*- coding: utf-8 -*-
from odoo import fields,models

class estatePropertytag(models.Model):
     _name = "estate.property.tag"
     _description = "This is regarding the real_estate"

     name = fields.Char(string='Name',required = True)
     
     _sql_constraints = [
          ('name_unique','UNIQUE(name)','Name must be unique!!')
     ]