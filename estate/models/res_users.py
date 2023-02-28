from odoo import models,fields


class ResUsers(models.Model):
    _name="res.users"
    _description="Res Users"
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property","salesperson_id")
    test = fields.Char()