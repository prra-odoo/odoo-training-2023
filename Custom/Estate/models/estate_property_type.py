from odoo import models,fields

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "New Estate Propert Type Module "

    name = fields.Char(required=True)

