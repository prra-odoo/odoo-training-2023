from odoo import models,fields

class BaseProperty(models.Model):
    _name="base.property"
    _description = "Base Property"

    base_price = fields.Integer()
    postcode = fields.Integer()
    base_date = fields.Date()

    

