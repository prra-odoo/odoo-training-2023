from odoo import fields, models

class Users(models.Model):
    _inherit="res.users"

    property_id=fields.One2many("estate.property","salesperson")
    nub = fields.Float()
    

