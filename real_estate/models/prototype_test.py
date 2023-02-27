from odoo import models,fields

class PrototypeTest(models.Model):
    _name = "prototype.test"
    _description="Testing Prototype Model"

    test=fields.Char()