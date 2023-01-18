# -*- coding: utf-8 -*-

from odoo import fields, models

class inheriteduser(models.Model):
    # _name= "try.model"
    # _inherits = {'res.users':'name_id'}
    _inherit = "res.users"


    property_ids = fields.One2many("estate.property","salesman_id",string="Properties", domain=[("state", "in", ["new", "offer_received"])])
    # name_id= fields.Many2one("res.users")
    demo=fields.Char("name")
