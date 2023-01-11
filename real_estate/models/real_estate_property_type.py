from odoo import models,fields
class RealEstatePropertyType(models.Model):
    _name="real.estate.property.type"
    _description="Property Type"
    name=fields.Char(string='Property Type',required=True)
    _sql_constraints_=[('type_unique','UNIQUE(name)','Type name should be unique')]