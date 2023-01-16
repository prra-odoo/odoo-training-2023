from odoo import models,fields
class RealEstatePropertyType(models.Model):
    _name="real.estate.property.type"
    _description="Property Type"
    _order="name"
    name=fields.Char(string='Property Type',required=True)
    property_ids=fields.One2many("real.estate.property","type_id")
    sequence=fields.Integer("Sequence",default=1)
    _sql_constraints_=[('type_unique','UNIQUE(name)','Type name should be unique')]