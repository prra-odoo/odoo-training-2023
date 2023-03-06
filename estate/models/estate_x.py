from odoo import models,fields,api

class EstateX(models.Model):
    _name = "estate.x"
    _description = "nothing"

    x = fields.Integer()
    y = fields.Char()