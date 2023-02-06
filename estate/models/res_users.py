# -*- coding: utf-8 -*-
from odoo import models,fields
from odoo.exceptions import UserError, ValidationError

class Users(models.Model):
    
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property","user_id", string="Property id")
