# -*- coding: utf-8 -*-

from odoo import models,fields

class open_academy(models.Model):
    _name : 'open.ecademy'
    _description :'Open academy'

    name = fields.Char('course name',required=True)