# -*- coding: utf-8 -*-
from odoo import fields,models

class EstatePrototype(models.Model):
    _name = "estate.prototype"
    _description = "Prototype Model for Inheritance"

    prototype_price = fields.Integer()
    prototype_postcode = fields.Char()
    prototype_date = fields.Date()