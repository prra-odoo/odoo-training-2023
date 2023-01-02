# -*- coding: utf-8 -*-

from odoo import models, fields

class estatepropertytype(models.Model):
    _name = "estate.property.type"
    _description="Property types module"

    name = fields.Char(string="Name",required=True)