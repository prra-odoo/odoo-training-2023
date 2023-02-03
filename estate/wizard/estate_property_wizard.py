# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyWizard(models.TransientModel):
    _name = "estate.property.wizard"
    _description = "new"

    price = fields.Float()
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)

    def action_done_wizard(self):
        pass
