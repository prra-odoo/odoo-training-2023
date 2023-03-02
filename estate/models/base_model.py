from odoo import models,fields


class BaseModel(models.Model):
    _name="base.model"
    _description="Base Model"
    
    price = fields.Char()
    date= fields.Date()
    postcode = fields.Char()
    test = fields.Char()