# -*- coding: utf-8 -*-
from random import randint
from odoo import fields,models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is Estate property tags model"
    _order = "name"
    # Table Fields
    name = fields.Char(required=True)
    
    # def _get_default_color(self):
    #     return randint(1,11)
    color= fields.Integer(string="Color")
    _sql_constraints = [
        ('unique_tag_name','unique(name)','Property Tag name should be unique!')
    ]