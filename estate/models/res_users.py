# -*- Coding: utf-8 -*-
from odoo import models, fields

class Users(models.Model):
	_inherit = 'res.users'

	property_ids = fields.One2many('estate.property', 'user_id', domain="[('state','in',['new','offer_recieved'])]")
	# test = fields.Char()