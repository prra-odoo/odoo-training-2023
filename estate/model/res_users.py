# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'salesperson_id', string="Property Name", domain=[('state','in',['new','offer_received'])])
    
