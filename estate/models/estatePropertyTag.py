# -- coding: utf-8 --

from odoo import fields,models


class estateProperty(models.Model):
    _name = "estate.property.tags"
    _description="property type model"
    _order="name"

    name=fields.Char(string="Property type",required=True)
    color=fields.Integer(string="color")

    sql_constraints = [
        ('check_type_uniqueness', 'unique(name)',
         'Type already exists.'),
    ]