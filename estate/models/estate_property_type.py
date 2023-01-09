# -*- coding: utf-8 -*-

from odoo import models,fields,api

class estatePropertyType(models.Model):
    _name ="estate.property.type"
    _description="This model defines the property type for Estate Property Module"
    _order = "sequence,name"

    name = fields.Char(required=True)
    sequence = fields.Integer(string="Sequence",default=1, help="Used to order Property types according to the user")
    property_ids=fields.One2many('estate.property','property_type_id',string="Property List")
    offer_count = fields.Integer('Property type count',compute="_compute_offer")
    offer_ids = fields.One2many("estate.property.offer","property_type_id",string = "Offers")
    _sql_constraints=[('property_type_unique','unique(name)','!!This property type is already there.')]

    @api.depends('offer_ids')
    def _compute_offer(self):
        for record in self:
            record.offer_count=len(record.offer_ids)
    


