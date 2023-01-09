from odoo import fields,models
class RealEstatePropertyTags(models.Model):
    _name="real.estate.property.tags"
    _description="Property Tags"
    name=fields.Char(string="Property Tags",required=True)