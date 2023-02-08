from odoo import models, fields


class EstatePropertyTypeModel(models.Model):
    _name = "estate.property.type"
    _description = "this is the Property Type Model"

    name = fields.Char(required=True)
    
