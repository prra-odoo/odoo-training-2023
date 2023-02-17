from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate property tag'

    name = fields.Char(required=True)

    _sql_constraints = [('name_uniq', 'unique(name)','The name must be unique')]