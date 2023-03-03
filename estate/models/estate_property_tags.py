from odoo import models,fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag field"
    _order = "name"
    _sql_constraints = [
        ('property_type_checker', 'unique(name)', 'This property type is already available.')
    ]
    
    name = fields.Char(required=True, inverse="_inverse_name")
    color = fields.Integer(string="Color")

    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()
