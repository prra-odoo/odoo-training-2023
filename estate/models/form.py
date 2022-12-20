# -*- coding: utf-8 -*-


from odoo import models, fields
 
class realEstate(models.Model):
    _name = "real_state"
    _description = "This is the Database for the all clients and their requirements"

    name = fields.Char( required=True )
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float( required =True )
    selling_price = fields.Float( required =True )
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('3BHK', 'Size'), ('Home','Type')]
        )
