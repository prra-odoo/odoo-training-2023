# -*- coding: utf-8 -*-

from odoo import fields,models

class InheritedResUser(models.Model):
    _name = "res.users"
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property","salesperson_id",string="Property Id")