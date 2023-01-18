# -*- coding: utf-8 -*-

from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"
    
    property_ids = fields.One2many("real.estate","salesperson_id",string="Property" , domain=[("state", "in", ["new", "offer_received"])])
    age = fields.Integer()
    name= fields.Char()
    #res.users have res.partner also in the db table so name field is shown in res.partner table