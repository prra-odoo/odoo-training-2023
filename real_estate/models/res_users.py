from odoo import models, fields


class resUsers(models.Model):
    _inherit = "res.users"


    property_ids = fields.One2many('estate.property', 'salesman_id', string="Property", domain=[("state", "in", ["new","received"])] )
    demo = fields.Char()
    