from odoo import models,fields
class RealEstatePropertyType(models.Model):
    _name="real.estate.property.type"
    _description="Property Type"
    name=fields.Char(string='Property Type',required=True)