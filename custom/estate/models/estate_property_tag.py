from odoo import models,fields 
class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="properties tags"
    name=fields.Char(required=True)
    _sql_constraints=[
        ('unique_tag','unique(name)','Tag names must be unique !')
        ]