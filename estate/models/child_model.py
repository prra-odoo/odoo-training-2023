from odoo import models, fields


class ChildModel(models.Model):
    _name = "child.model"
    _description = "Child Model"

    _inherit = "base.model"

    phone = fields.Char()
