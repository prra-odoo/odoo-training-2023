# -- coding: utf-8 --

from odoo import fields,models


class estateProperty(models.Model):
    _name = "estate.property.type"
    _description="property type model"

    name=fields.Char(string="Property type",required=True, readonly=True,)
    properties_in_this_type_ids=fields.One2many("estate.property", "property_type_id", string="properties in type")
