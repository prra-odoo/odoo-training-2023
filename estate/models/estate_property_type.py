from odoo import api,models,fields

class EstatePropertyType(models.Model):
	_name='estate.property.type'
	_description='adding property type in property'
	_order='name'

	name=fields.Char(string='Name',
			required=True,
			help="this is for property type name")
	
	_sql_constraints=[
		('ptype_name_uniq','unique (name)','Property Type name must be unique.')
	]

	property_ids=fields.One2many("estate.property","property_type_id")
		
	sequence=fields.Integer(string="Sequence",default=1,help="use of handle widget")

	offer_ids=fields.One2many("estate.property.offer","property_type_id")
	offer_count=fields.Integer(compute="_compute_count")
	@api.depends("offer_ids")
	def _compute_count(self):
		for record in self:
			if record.offer_ids:
				record.offer_count=len(record.offer_ids)
			else:
				record.offer_count=0