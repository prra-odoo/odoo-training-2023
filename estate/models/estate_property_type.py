# -*- coding: utf-8 -*-

from odoo import models, fields

class estatepropertytype(models.Model):
    _name = "estate.property.type"
    _description="Property types module"

    name = fields.Char(string="Name",required=True)
    propertyname = fields.One2many("estate.property","property_id",string="Present Properties")

    _sql_constraints = [
        ('checktype', 'unique (name)', "Property name cannot be similar"),
    ]