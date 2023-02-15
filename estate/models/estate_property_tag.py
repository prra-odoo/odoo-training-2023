# -*- coding: utf-8 -*-
from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag Model"

    name = fields.Char(required=True)
