from odoo import models,fields

class BaseProperty(models.Model):
    
    _name="base.property"
    _description = "Base Property which is to be inherited"

    pricee = fields.Integer()
    postcode = fields.Integer()
    datee = fields.Date()