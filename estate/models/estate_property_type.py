# -*- coding: utf-8 -*-
from odoo import models,fields,api

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description="estate property type"
    _order = "sequence,name"

    name= fields.Char("Type" ,required=True)
    property_ids = fields.One2many('estate.property','property_type_id', string = "All property")
    sequence = fields.Integer('Sequence', default =1)
    offer_ids = fields.One2many('estate.property.offer','property_type_id',string = "OfferIds")
    offer_count = fields.Integer(compute = "_count_total_offers" )


    _sql_constraints = [
        (
            'check_property_uniqueness' , 'unique(name)',
            "Property name already exist in the database"

        )
    ]

    @api.depends("offer_ids")
    def _count_total_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
