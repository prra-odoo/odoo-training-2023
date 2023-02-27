from odoo import fields,models

class EstatePrototype(models.Model):
    _name = "estate.prototype"
    _description = "Estate Prototype Model"
    
    price = fields.Float()
    postcode = fields.Char()
    date = fields.Date()