from odoo import models,fields

class EstatePropertyTagModel(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate.property.tag'
    _sql_constraints = [
        (
            'unique_property_tag',
            'unique (name)',
            'Tag name should be Unique'
        )
    ]
    _order="name"

    name=fields.Char(string="Tag Name",required=True)
    color=fields.Integer()
