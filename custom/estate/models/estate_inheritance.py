from odoo import fields,models,api
class EstateInheritance(models.Model):
    _name="estate_inheritance"
    price=fields.Integer()
    postcode=fields.Char()
    date=fields.Date()
    


