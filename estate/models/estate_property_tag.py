# -*- coding: utf-8 -*-

from odoo import models,fields

class esattePropertyTags(models.Model):
	_name ='estate.property.tag'
	_description ='This is a model to represent estate property tags'
	_order = "name"

	name=fields.Char(string='Name',required=True)
	color = fields.Integer()
	_sql_constraints=[('property_tag_name_unique','unique(name)','Property tag name must be unique')]
