# -*- coding: utf-8 -*-
from odoo import models

class inherited_model(models.Model):
    _inherit='real.estate.properties'

    def action_sold(self):
        print("....................................hello")
        return super().action_sold()