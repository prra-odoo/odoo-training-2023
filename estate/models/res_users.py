# -*- coding: utf-8 -*-
from odoo import models,fields
from odoo.exceptions import UserError, ValidationError

class Res_Users(models.Model):
    _name = "res.users"
    _description = "users model"

    property_ids = fields.One2many("estate.property","user_id", string="Property id")
