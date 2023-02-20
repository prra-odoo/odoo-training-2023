from odoo import models,fields

class EstatePropertyType(models.Model):
	_name='estate.property.type'
	_description='adding property type in property'

	name=fields.Char(string='Name',
			required=True,
			help="this is for property type name")
	
	_sql_constraints=[
		('ptype_name_uniq','unique (name)','Property Type name must be unique.')
	]

	property_ids=fields.One2many("estate.property","property_type_id")


	