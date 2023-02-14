from odoo import models,fields

class AcomPropertyManagerModel(models.Model):
    _name = "acom.prop.manager"
    _description = "this is the Property Type Model"

    name = fields.Char(required=True)