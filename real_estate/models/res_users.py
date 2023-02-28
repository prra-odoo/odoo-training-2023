from odoo import models,fields

class ResUsers(models.Model):
    _inherit = "res.users"

    new_field=fields.Char()

    property_ids=fields.One2many('estate.property','salesmen_id')
