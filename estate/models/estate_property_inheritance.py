from odoo import models,fields

class EstatePropertyInheritance(models.Model):
    _name="estate.property.inheritance"
    _inherit="estate.property"
    _description="Estate Property Inheritance"

    date=fields.Date()
    price=fields.Float()
    postcode=fields.Char()