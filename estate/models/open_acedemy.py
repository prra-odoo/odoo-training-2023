# -*- coding: utf-8 -*-

from odoo import fields,models

class OpenAcedemy(models.Model):
    _name = 'open.acedemy'
    _description = "this is a open acedemy course module"

    name = fields.Char()