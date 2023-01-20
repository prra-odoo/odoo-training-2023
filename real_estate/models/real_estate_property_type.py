from odoo import models,fields,api
class RealEstatePropertyType(models.Model):
    _name="real.estate.property.type"
    _description="Property Type"
    _order="name"
    name=fields.Char(string='Property Type',required=True)
    property_ids=fields.One2many("real.estate.property","type_id")
    sequence=fields.Integer("Sequence",default=1)
    offer_ids=fields.One2many("real.estate.property.offer","property_type_id")
    offer_count=fields.Integer(compute="_compute_offer_count")
    _sql_constraints_=[('type_unique','UNIQUE(name)','Type name should be unique')]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count=len(record.offer_ids)