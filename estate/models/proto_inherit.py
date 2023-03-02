from odoo import models, fields


class ProtoInher(models.Model):
    _inherit = "estate.property"
    _name = "proto.inherit"
    _description = "Prototype Inheritance Demo"

    price = fields.Float()
    postcode = fields.Integer()
    date = fields.Date()
