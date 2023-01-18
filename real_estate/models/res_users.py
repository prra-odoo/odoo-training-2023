# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,models,fields

class InheritedUsers(models.Model):
    _inherit='res.users'

    property_ids=fields.One2many('estate.properties', 'salesperson_id', string="inherited users", domain="['|', ('state', '=', 'new'), ('state', '=', 'offer_received')]")