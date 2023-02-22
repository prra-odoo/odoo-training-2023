from odoo import models,fields,_,api

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "New Estate Propert Type Module "
    _order="sequence,name"

    name = fields.Char(required=True)
    property_ids =fields.One2many('estate.property','property_type_ID')
    sequence=fields.Integer('Sequence',default=1,help="sequence_manually")
    # offer_ids= fields.One2many("estate-property.offer","property_type_id")
    # offer_count = fields.Integerr(compute="_count_offers")

    _sql_constraints=[(
        'property_type_unique',
        'unique(name)',
        'Property Type must be Unique.'
    )]

    # @api.depends("offer_ids")
    # def _count_offers(self):
    #     for record in self:
    #         record.offer_count= record.offer_ids
