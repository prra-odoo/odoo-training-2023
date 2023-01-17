from odoo import fields,models

class inherited_model(models.Model):
    _inherit='res.users'

    property_ids=fields.One2many("real.estate.properties","user_id")
