# -*- coding: utf-8 -*-
from odoo import api,fields, models, _
from odoo.exceptions import UserError


class estateProperty(models.Model):
    _inherit = "estate.property"
    _description = "Inherit Estate Model"
    
    def action_sold(self):
        print('djsnkf')
        return super().action_sold()
        