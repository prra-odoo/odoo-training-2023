from odoo import models,api,fields

class InheritFields(models.Model):
    _name="inherit.fields"

    textvalue=fields.Char()
