from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name="estate.property.tags"
    _description="Esatet Property Tags"
    
    name = fields.Char(required = True)