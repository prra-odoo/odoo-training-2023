# -*- coding: utf-8 -*-

from odoo import models, fields

class ResUsersInherited(models.Model):
    _name = "res.users"
    _inherit = "res.users"
    
    property_ids = fields.One2many("estate.property", "salesperson_id", string="Property IDs", domain=['|',('state', '=' , 'new'),('state','=','offer_recieved')]) 
    