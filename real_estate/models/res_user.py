# -*- coding: utf-8 -*-

from odoo import models, fields

class res_user(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'salesperson_id', domain=[("state", "in", ['new', 'offer_received'])])
