from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name="estate.property.tags"
    _description="Esatet Property Tags"
    
    name = fields.Char(required = True)
    
    _sql_constraints = [
        ("unique_tags","unique(name)","The name must be unique"),
    ]