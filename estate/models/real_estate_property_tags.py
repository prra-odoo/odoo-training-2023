from odoo import models,fields

class EstatePropertyTagModel(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate.property.tag'

    name=fields.Char(string="Name",required=True)
    