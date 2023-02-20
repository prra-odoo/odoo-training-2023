# -- coding: utf-8 --

from odoo import fields,models,api


class estateProperty(models.Model):
    _name = "estate.property.type"
    _description="property type model"
    _order="name"

    name=fields.Char(string="Property type",required=True,)
    property_ids=fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    offer_ids=fields.One2many("estate.property.offer","type_id","Offers")
    offer_count=fields.Integer(compute="_compute_offers",default=0)
    @api.depends('offer_ids')
    def _compute_offers(self):
        for record in self:
            record.offer_count=len(record.offer_ids)

    _sql_constraints = [
        ('check_type_uniqueness', 'unique(name)',
         'Type already exists.'),
    ]   