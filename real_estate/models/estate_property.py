# -*- coding: utf-8 -*-

from odoo import models, fields

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate module properties"

    name = fields.Char(string="Title" ,required=True)
    expected_price = fields.Float(string="Expected Price", required=True, help='What is your expected price of the property?')
    