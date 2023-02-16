from odoo import models,fields,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type field"
    _order = "sequence, name, id" # by default order is ascending 

    name = fields.Char(required=True, inverse="_inverse_name")
    property_ids = fields.One2many('estate.property','property_type_id',string="Properties")
    sequence = fields.Integer(string='Sequence', default = 1, help="Used to properties stages")


    _sql_constraints = [
        ('property_type_checker', 'unique(name)', 'This property type is already available.')
    ]
    
    # @api.depends('name')
    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()

    