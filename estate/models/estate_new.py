from odoo import models, fields, _

class EstateNew(models.Model):
    _name = "estate.new"
    _description = "estate property demo field"
    # _inherit = "estate.property"

    price_demo = fields.Integer(string = "Price")
    postcode_demo = fields.Integer(string = "PostCode")
    date_demo = fields.Date(string = "Demo Date")