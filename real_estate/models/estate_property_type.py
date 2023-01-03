# -*- coding:utf:8 -*-

from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Type module"

    name = fields.Char(string='Name', required=True)