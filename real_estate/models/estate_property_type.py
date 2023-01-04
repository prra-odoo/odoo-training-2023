# -*- coding:utf:8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Type module"
    _order = "name desc"

    name = fields.Char(string='Name', required=True)
    offer_ids = fields.One2many("estate.property","property_type_id",string="Offer")
    sequence = fields.Integer('Sequence')

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'Name must be unique')
    ]
