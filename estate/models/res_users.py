# -*- coding: utf-8 -*-

from odoo import models,fields

class Users(models.Model):
    _inherit="res.users"

    property_ids = fields.One2many("estate.property","sales_id",domain=[('state','in',['new'])])
