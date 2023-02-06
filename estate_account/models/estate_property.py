# -*- coding: utf-8 -*-

from odoo import models

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold_btn(self):
        for record in self:
            print("===============")
            print(record.status)

            return super().action_sold_btn()
