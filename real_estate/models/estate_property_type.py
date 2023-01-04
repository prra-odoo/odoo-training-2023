from odoo import fields, models

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "name"

    name = fields.Char('Name', required = True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer('Sequence', default=1)

    _sql_constraints = [
            ('name_uniq', 'unique (name)', "Property Type already exists !"),
    ]