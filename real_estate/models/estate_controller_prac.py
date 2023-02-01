from odoo import models, fields, api

class Contoller_Practice(models.Model):
    _name = 'estate.controller.practice'
    _description = 'This is just to learn controller'

    name = fields.Char()
    biography = fields.Html()