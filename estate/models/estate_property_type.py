# -*- coding: utf-8 -*-
from odoo import models,fields

class Estate_Property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char(string = 'name',required=True)
