# -*- coding: utf-8 -*-
from odoo import fields, models


class Prototype(models.Model):
	_name = "prototype.prototype"
	_description = "Prototype Test Model"

	test_price = fields.Float()
	test_postcode = fields.Integer()
	test_date = fields.Date()