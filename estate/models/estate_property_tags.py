from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name="estate.property.tags"
    _description="Esatet Property Tags"
    
    name = fields.Char(required = True)
    color = fields.Integer(string="Color")
    _order = "name"
    _sql_constraints = [
        ("unique_tags","unique(name)","The name must be unique"),
    ]