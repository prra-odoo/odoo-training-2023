# -*- coding: utf-8 -*-
from odoo import models,fields

class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property tag"
    _order = "name"

    name = fields.Char(required = True)
    color = fields.Integer()




    _sql_constraints = [
        (
            'check_property_tag_uniqueness' , 'unique(name)',
            "Property tag already exist in the database"

        )
    ]
    