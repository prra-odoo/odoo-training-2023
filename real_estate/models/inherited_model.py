from odoo import fields,models

class inherited_model(models.Model):
    # _name="inherited.model"
    _inherit='res.users'

    property_ids=fields.One2many("real.estate.properties","salesperson")
    # name=fields.Char()
    price=fields.Char()