# -- coding: utf-8 --
from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type Model"
    _order = "sequence,name asc"
    
    name = fields.Char(required=True)   
    property_ids = fields.One2many("estate.property", "property_type_id")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    offer_ids = fields.One2many('estate.property.offers',"property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    _sql_constraints = [
        ('property_type_unique',
        'unique(name)',
        'The Property Type must be unique!!')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    # @api.depends('offer_ids')
    # def _compute_offer_count(self):
    #     if self.offer_ids:
    #         self.offer_count=self.env['estate.property.offers'].search_count([('property_type_id','=',self.name)])
    #     else:
    #         self.offer_count=0