from odoo import models,fields

class EstateTagProperty(models.Model):
    _name="real.estate.property.tag"
    _description="Property Tag Model"

    name=fields.Char(string="name",required=True)
    description=fields.Text('Description')
    
    
