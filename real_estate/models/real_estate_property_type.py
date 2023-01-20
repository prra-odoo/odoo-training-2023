from odoo import fields, models,api


class RealEstatePropertyType(models.Model):
    _name = "real.estate.property.type"
    _description = "Property Type"
    _order = "name"

    name = fields.Char(string="Property Type", required=True)
    active = fields.Boolean(default=True)
    property_ids = fields.One2many("real.estate.property", "property_type_id", string="Property_ids")
    sequence = fields.Integer('Sequence', default=1, help="Used to order property")
    offer_ids = fields.One2many("real.estate.property.offer", "property_type_id", string="Offer_id")
    offer_count = fields.Integer(compute="_compute_number_of_offers")
    
    _sql_constraints = [('unique_type_name', 'UNIQUE(name)','The Name of an property type must be unique.')]
    
    @api.depends("offer_ids")
    def _compute_number_of_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
