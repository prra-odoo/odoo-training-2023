# -*- coding: utf-8 -*-


from attr import fields
from odoo import models

class Estateproperty(models.Model):
      _name = "Estateproperty.model"
      _description = "real_estate_property"

      name = fields.Char(required=True)    
      description = fields.Text(required=True)
      postcode = fields.Char(required=True)
      date_availability=fields.Date(required=True)
      



