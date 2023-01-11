# -*- coding: utf-8 -*-

from odoo import models, fields

class estateTag(models.Model):
    _name = "estate.property.tag"
    _description = "This module of estate property tag"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique")
    ]
    name = fields.Char("Name",required=True)
    pincode = fields.Integer(string="Pincode")
    colors = fields.Integer("Color Index")
    sequences = fields.Integer("Sequence")