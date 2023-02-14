from odoo import models,fields

class AcomPropertiesModel(models.Model):
    _name = "acom.properties"
    _description = "this is the Property Type Model"

    name = fields.Char(required=True)