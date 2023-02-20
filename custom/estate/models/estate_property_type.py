from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate property type'
    _order = 'property_name'
    _rec_name = 'property_name'

    property_name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer(default=1)
    
    _sql_constraints = [('property_name_uniq', 'unique(property_name)','The name must be unique')]