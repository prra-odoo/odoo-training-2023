from odoo import fields, models


class RealEstatePropertyTags(models.Model):
    _name = "real.estate.property.tags"
    _description = "Property Tags"
    _order = "name"

    name = fields.Char(string="Tags", required=True)
    color = fields.Integer()
    
    _sql_constraints = [('unique_name', 'UNIQUE(name)','The Name of an property tag must be unique.')]