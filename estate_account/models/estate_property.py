# -*- coding: utf-8 -*-


from odoo import fields, models


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def sold_buisness_logic(self):
        # self.env["estate.property"]

        return super().sold_buisness_logic()
