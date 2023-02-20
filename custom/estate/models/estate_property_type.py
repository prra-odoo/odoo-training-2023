from odoo import models,fields
class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Property Type must be unique'),
    ]
    _order="sequence , name"


    name=fields.Char()
    property_ids=fields.One2many('estate.real.property','property_type_id',string="types")
    sequence=fields.Integer(default=1)

    

