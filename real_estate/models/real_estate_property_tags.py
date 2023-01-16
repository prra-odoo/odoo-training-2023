from odoo import fields,models
class RealEstatePropertyTags(models.Model):
    _name="real.estate.property.tags"
    _description="Property Tags"
    _order="name"
    name=fields.Char(string="Property Tags",required=True)
    color=fields.Integer("Color")
    _sql_constraints_=[('tag_unique','UNIQUE(name)','Tag name should be unique')]