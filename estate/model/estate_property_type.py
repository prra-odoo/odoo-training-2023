# -*- coding: utf-8 -*-
from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real estate advertisement module types"

    name = fields.Char('Name',required=True)