# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError


class users1(models.Model):
    _name = 'users.users'
    _description = "Real Estate Module"

    name = fields.Char('sale_person')
    property_ids = fields.One2many('estate.property','salesperson',string="properties")