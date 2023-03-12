from odoo import models,fields,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type field"
    _order = "sequence, name, id" # by default order is ascending 
    _sql_constraints = [
        ('property_type_checker', 'unique(name)', 'This property type is already available.')
    ]
    
    name = fields.Char(required=True, inverse="_inverse_name")
    property_ids = fields.One2many('estate.property','property_type_id',string="Properties")
    sequence = fields.Integer(string='Sequence', default = 1, help="Used to properties stages")
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id',string="Offer id")
    offer_count = fields.Integer(string="Offer Count",  default=0, inverse = "_inverse_offer_count")

    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()

    def _inverse_offer_count(self):
        for record in self:
            record.offer_count=len(record.offer_ids)

    