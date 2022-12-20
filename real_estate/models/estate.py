# -*- coding: utf-8 -*-

from odoo import fields,models

class estate(models.Model):
     _name = "real_estate.model"
     _description = "This is regarding the real_estate"

     name = fields.Char()
     description = fields.Text()
     postcode = fields.Char()
     date_availability = fields.Date()
     expected_price = fields.Float()
     selling_price = fields.Float()
     bedrooms = fields.Integer()
     living_area = fields.Integer()
     facades = fields.Integer()
     garage = fields.Boolean()
     garden = fields.Boolean()
     garden_area = fields.Integer()
     #garden_orientation = fields.Selection()
