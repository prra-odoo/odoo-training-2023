from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'teachers'
    _description = "This is a teachers model."

    name = fields.Char()
    biography = fields.Html()
