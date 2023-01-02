# -*- coding: utf-8 -*-
from odoo import models,fields

class estate_Property(models.Model):
      _name = "estate_property"
      _description = "real_estate_property"

      name = fields.Char(required=True)    
      description = fields.Text()
      postcode = fields.Char()
      date_availability=fields.Date()
      expeccted_price=fields.Float()
      selling_price=fields.Float()
      bedroom=fields.Integer()
      living_area=fields.Integer()

      garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('east', 'East'),('west', 'west'),('south', 'South')],
        help=("used for the garden orientation"))
      active = fields.Boolean('Active', readonly=True)







