# -- coding: utf-8 --
from odoo import models, fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "estate property tags Model"
    
    name = fields.Char(required=True)   