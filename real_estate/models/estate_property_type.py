# -*- coding: utf-8 -*-
from odoo import models,fields

class estate_property_type(models.Model):
    _name = 'estate.property.type'
    _description = "Estate Property Type"

    name = fields.Char("Property type",required=True)