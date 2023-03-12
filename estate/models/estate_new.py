from odoo import models, fields, _

class EstateNew(models.Model):
    _name = "estate.new"
    _description = "estate property demo field"

    price_demo = fields.Integer(string = "Price Demo")
    postcode_demo = fields.Integer(string = "PostCode Demo")
    date_demo = fields.Date(string = "Trial Date")