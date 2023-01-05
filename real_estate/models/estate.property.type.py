from odoo import models,fields

class EstateTypeProperty(models.Model):
    _name="real.estate.property.type"
    _description="Property Type Model"

    name=fields.Char(string="Title",required=True)
    description=fields.Text('Description')
