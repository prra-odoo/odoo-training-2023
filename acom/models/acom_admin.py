from odoo import models,fields

class AcomAdminModel(models.Model):
    _name = "acom.admin"
    _description = "this is the Property Type Model"

    name = fields.Char(required=True)