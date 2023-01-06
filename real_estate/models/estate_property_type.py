# -*- coding: utf-8 -*-
from odoo import models,fields

class estate_Property_type(models.Model):
      _name = "estate.property.type"
      _description = "Real estate based advertisedment module for the property type"

      name = fields.Char(required=True)