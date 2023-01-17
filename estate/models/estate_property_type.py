# -*- coding: utf-8 -*-
from odoo import fields, models


class estate_property_type(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"

    name=fields.Char(string="Name",required=True)