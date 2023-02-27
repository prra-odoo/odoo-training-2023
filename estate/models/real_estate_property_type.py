from odoo import api, models, fields

class EstatePropertyTypeModel(models.Model):
    _name = "estate.property.type"
    _description = "this is the Property Type Model"
    _sql_constraints = [
        (
            'unique_property_type',
            'unique (name)',
            'Property Type should be Unique'
        )
    ]
    _order="name desc"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer('sequence', help="Used to order property types")
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer(string="Offer Count",default=0, compute="_compute_offer_count")

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)