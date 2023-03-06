from odoo import models , fields

class EstateInheritance(models.Model):
    _name="estate.inheritance"
    _description="this is a model for learning inheritance"


    postcode =fields.Char()
    price =fields.Integer()
    date=fields.Date()