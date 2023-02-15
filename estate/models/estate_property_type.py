from odoo import models,fields,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type field"

    name = fields.Char(required=True, compute="_compute_name")

    @api.depends('name')
    def _compute_name(self):
        for record in self:
            tempname = record.name.split(' ')
            record.name = record.name.join(temp.title() for temp in tempname[0:])

    _sql_constraints = [
        ('property_type_checker', 'unique(name)', 'This property type is already available.')
    ]