from odoo import models,fields

class EstatePropertyType(models.Model):
	_name='estate.property.type'
	_description='adding property type in property'

	name=fields.Char(string='Name',
			required=True,
			help="this is for property type name")
	