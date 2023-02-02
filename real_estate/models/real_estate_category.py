from odoo import models, api, fields

class EstateCategory(models.Model):
    _name="estate.category"

    name = fields.Char()
    description = fields.Html()