from odoo import models,fields
from datetime import datetime

class EstateInherit(models.Model):
    _name = 'estate.inherit'
    _description = 'estate inheritance'

    price1 = fields.Char()
    postcode1 = fields.Integer()
    date1 = fields.Date(default=datetime.today())