# -*- coding: utf-8 -*-

from odoo import models

class estateProperty(models.Model):
    _inherit= "estate.property"
    
    def action_sold(self):
        print("Hello")
        return super(estateProperty,self).action_sold()
    