from odoo import fields,models,api

class Resusers(models.Model):
    _inherit="res.users"

    property_ids = fields.One2many("estate.property.model","salesperson_id")
    