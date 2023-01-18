# -*- coding: utf-8 -*-

from odoo import models,fields

class inheritedModel(models.Model):
    _inherit="res.users"

    property_ids = fields.One2many("estate.property","sales_id")
    name=fields.Char()
    nameusers=fields.Many2one("estate.property","name")
    abc=fields.Char()

