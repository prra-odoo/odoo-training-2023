from odoo import fields, models
 

class propertyType(models.Model):
    _name="estate.property.type"
    _description = "property type model"
    _order = "name"

    name = fields.Char('Name')
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer("Sequence", default=3)
    offer_ids = fields.One2many('estate.property.offer','property_type_id',string='Estate Offer')
    offer_count=fields.Integer(string="offer count",compute='_compute_offer_count')

    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
