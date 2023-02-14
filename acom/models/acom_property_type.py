from odoo import models,fields

class AcomPropertyTypeModel(models.Model):
    _name = "acom.property.type"
    _description = "this is the Property Type Model"

    name = fields.Char(required=True)