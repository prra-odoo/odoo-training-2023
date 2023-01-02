# -*- coding: utf-8 -*-

from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.order"
    _description = "This model will store the price related to estate"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Address of the building")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = "Type",
        selection = [("north", "North"), ("south", "South"), ("west", "West"), ("east", "East")]
    )




