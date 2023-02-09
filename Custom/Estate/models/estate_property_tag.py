from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _description= 'Creating an many to many property tag '

    name= fields.Char(required=True)
