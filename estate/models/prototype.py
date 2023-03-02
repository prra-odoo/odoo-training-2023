# -*- coding: utf-8 -*-
from odoo import models, fields

class Prototype(models.Model):
	_name = "prototype.prototype"
	_description = "This is prototype model"

	a = fields.Float()
	b = fields.Char()
	c = fields.Date()