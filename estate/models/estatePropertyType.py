# -- coding: utf-8 --

from odoo import fields,models


class estateProperty(models.Model):
    _name = "estate.property.type"
    _description="property type model"
    _order="name"

    name=fields.Char(string="Property type",required=True,)
    property_ids=fields.One2many("estate.property", "property_type_id", string="properties in type")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    sql_constraints = [
        ('check_type_uniqueness', 'unique(name)',
         'Type already exists.'),
    ]