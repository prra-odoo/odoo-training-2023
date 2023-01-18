# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'salesperson_id', string="Property Name", domain=[('state','in',['new','offer_received'])])
    demo = fields.Integer()

# class NewResUser(models.Model):
#     _name = 'new.res.user'
#     _inherits = {'estate.property.offer':'offer_id'}

#     offer_id = fields.Many2one('estate.property.offer','delegation field')
#     newdemo = fields.Integer()