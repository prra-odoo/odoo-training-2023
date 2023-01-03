# -*- coding:utf:8 -*-

from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Tag module"

    name = fields.Char(required=True)