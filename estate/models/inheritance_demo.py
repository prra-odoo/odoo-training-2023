from odoo import models,fields


class InheritanceDemo(models.Model):
    _name = "inheritance.demo"
    _description = "Inheritance demo"

    price = fields.Float(default = 0)
    postcode_demo = fields.Integer()
    deadline = fields.Date(default = fields.Date().today())
