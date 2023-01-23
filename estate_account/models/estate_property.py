# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateAccount(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        return super().action_sold()