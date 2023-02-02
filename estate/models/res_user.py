# -- coding: utf-8 --
from odoo import fields,models,api

class resUser(models.Model):
    _name = "res.user"
    _inherit="res.user"

    property_ids=fields.One2many("estate.property","salesperson_id",string="Properties")