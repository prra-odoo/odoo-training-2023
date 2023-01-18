# -*- coding: utf-8 -*-

from odoo import models

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def property_sold(self):
        return super().property_sold