from odoo import models,fields

class PrototypeTest(models.Model):
    _name = "prototype.test"
    _description="Testing Prototype Model"

    price = fields.Float()
    postcode = fields.Integer()
    date = fields.Date()