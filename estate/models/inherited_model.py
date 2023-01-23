from odoo import models , fields

class inheritedModel(models.Model):
	_inherit = "res.users"

	property_ids = fields.One2many('estate.property','salesman_id',string="Real Estate Property")


# class prototypeInheritance(models.Model):
# 	_name = "altaf.estate"
# 	_inherit = "estate.property"
# 	_description="This model is just for describing the prototype inheritance"


# class delegationInheritance(models.Model):
# 	_name = "new_users"
# 	_inherits = {'res.partner': 'partner_id'}

# 	partner_id = fields.Many2one('res.partner')
# 	val = fields.Char(related="partner_id.val",inherited=True,required=True,store=True)

