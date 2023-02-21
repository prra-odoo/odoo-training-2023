from odoo import api,models,fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate property type'
    _order = 'property_name'
    _rec_name = 'property_name'

    property_name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer()

    offer_ids = fields.One2many('estate.property.offer', 'property_type_id') 
    offer_count = fields.Integer(compute='_compute_offer_count', store=True) 
    
    _sql_constraints = [('property_name_uniq', 'unique(property_name)','The name must be unique')]