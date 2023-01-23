# -*- coding: utf-8 -*-

from odoo import models,fields

class inheritedModel(models.Model):
    _inherit="res.users"

    name=fields.Char()
    abc=fields.Char()
    nameusers=fields.Many2one("estate.property","name")
    property_ids = fields.One2many("estate.property","sales_id",domain=[('state','in',['new'])])
