# -*- coding: utf-8 -*-
from odoo import fields,models

class estateProperty(models.Model):
     _name = "estate.property.type"
     _description = "This is regarding the real_estate"

     name = fields.Char(string='Name',required = True)