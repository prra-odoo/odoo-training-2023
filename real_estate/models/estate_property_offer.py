# -*- coding: utf-8 -*-
from odoo import models,fields

class estate_property_offers(models.Model):
    _name = 'estate.property.offer'
    _description = "Estate Property Offers"

    price = fields.Float('Price',required=True)
    status = fields.Selection(
            string='Status',copy=False,
            selection=[('refused','refused'),('accepted','accepted')])
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    
