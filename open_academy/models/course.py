# -*- coding: utf-8 -*-

from odoo import models, fields

class openAcademyCourse(models.Model):
	_name = 'academy.course'
	_description = 'Open Academy Model for Course'

	name = fields.Char('Name', required=True)
	description = fields.Text(default='basic description', copy=False)
	date = fields.Date('Date', default=lambda self: fields.Date.today(), readonly=True)
	active = fields.Boolean(default=True)
	state = fields.Selection([('new', 'New'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default="new")
