from odoo import models,fields

class InheritedModel(models.Model):
    _inherit="res.users"
    property_ids=fields.One2many("real.estate.property","salesman_id")