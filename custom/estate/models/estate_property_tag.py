from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate property tag'
    _order = 'name'

    name = fields.Char()
    color = fields.Integer()

    _sql_constraints = [('name_uniq', 'unique(name)','The name must be unique')]