from odoo import models,fields

class EstatePropertyTag(models.Model):
	_name='estate.property.tag'
	_description='adding property tags in property'

	name=fields.Char(string='Name',
			required=True,
			help="this is for property tag name")