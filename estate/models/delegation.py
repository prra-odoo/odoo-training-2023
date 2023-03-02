# -*- coding: utf-8 -*-
from odoo import models, fields

class Delegation(models.Model):

	_name = "delegation.abc"
	_description = "Check Delegation Inherit"
	_inherits = {'estate.property': 'deleg_id'}

	deleg_id = fields.Many2one('estate.property', required=True, ondelete="cascade")
	check = fields.Char()
	