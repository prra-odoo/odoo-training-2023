# -*- coding: utf-8 -*-
from odoo import models,fields

class Estate_Property_Tag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"

    name = fields.Char(string = 'name',required=True)