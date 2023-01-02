# -*- coding: utf-8 -*-

from odoo import models,fields

class esattePropertyTags(models.Model):
	_name ='estate.property.tag'
	_description ='This is a model to represent estate property tags'

	name=fields.Char('Name',required=True)
