# -*- coding: utf-8 -*-
from odoo import fields, models

class estate_property_tag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag model"

    name=fields.Char(string="Name",required=True)