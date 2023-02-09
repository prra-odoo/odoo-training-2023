from odoo import models, fields

class EstatePropertyType(models.Model):
    _name= "estate.property.type"
    _description = "this is a estate property module "

    name = fields.Char(required=True)