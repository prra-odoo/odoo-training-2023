# -*- coding: utf-8 -*-

from odoo import models,fields

class esattePropertyTags(models.Model):
	_name ='estate.property.tag'
	_description ='This is a model to represent estate property tags'

	name=fields.Char('Name',required=True)
	_sql_constraints=[('property_tag_name_unique','unique(name)','Property tag name must be unique')]
