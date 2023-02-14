from odoo import models,fields

class AcomPropertyTenantModel(models.Model):
    _name = "acom.prop.tenant"
    _description = "this is the Property Type Model"

    name = fields.Char(required=True)