from odoo import models,fields

class EstatePropertySettingsModel(models.Model):
    _name="estate.purchase"
    _description="this is the Estate settings Model"

    name = fields.Char(required=True)
    description = fields.Text()
