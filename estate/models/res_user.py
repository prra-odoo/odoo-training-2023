# -- coding: utf-8 --
from odoo import fields,models,api

class resUsers(models.Model):
    _name = "res.users"
    _inherit="res.users"

    property_ids=fields.One2many("estate.property","salesperson_id",string="Properties")