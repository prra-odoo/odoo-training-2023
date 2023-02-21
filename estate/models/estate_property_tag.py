from odoo import models,fields

class EstatePropertyTag(models.Model):
	_name='estate.property.tag'
	_description='adding property tags in property'
	_order='name'

	name=fields.Char(string="Name",
		required=True)

	_sql_constraints=[
		('ptag_name_uniq','unique (name)','Property Tag name must be unique.')
	]

	color=fields.Integer(string="Color")