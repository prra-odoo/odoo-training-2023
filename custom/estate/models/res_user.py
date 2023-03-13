from odoo import fields,models

class ResUser(models.Model):
    _name="res.users"
    _inherit ="res.users"
    property_ids=fields.One2many('estate.real.property','seller_id',string="user")