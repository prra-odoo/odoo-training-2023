from odoo import fields, models


class RealEstatePropertyTags(models.Model):
    _name = "real.estate.property.tags"
    _description = "Property Tags"

    name = fields.Char(string="Tags", required=True)
    color = fields.Integer(default=3)
    
    _sql_constraints = [('unique_name', 'UNIQUE(name)','The Name of an property tag must be unique.')]