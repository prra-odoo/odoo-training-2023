# -*- coding: utf-8 -*-

from odoo import models, fields

class openAcademyCourse(models.Model):
	_name = 'academy.course'
	_description = 'Open Academy Model for Course'

	name = fields.Char('Name', required=True, readonly=True, copy=False)
	description = fields.Text(default='basic description')
	date = fields.Date('Date', default=lambda self: fields.Date.today())
