# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError


class EstateProperty(models.Model):
    _inherit = "estate.property"

    name = fields.Char()
    
