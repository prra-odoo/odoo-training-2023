# -*- coding: utf-8 -*-

from odoo import models, fields

class estate_property_tags(models.Model):
    _name = "estate.property.tags"
    _description="Property tags module"

    name = fields.Char(string="Name",required=True)