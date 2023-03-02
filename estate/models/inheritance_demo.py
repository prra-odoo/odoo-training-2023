from odoo import models,fields


class InheritanceDemo(models.Model):
    _name = "inheritance.demo"
    _description = "Inheritance demo"
    _inherits = {'res.partner' : 'partner_id'}

    price = fields.Float(default = 0)
    postcode_demo = fields.Integer()
    deadline = fields.Date(default = fields.Date().today())
    partner_id = fields.Many2one("res.partner")

    
