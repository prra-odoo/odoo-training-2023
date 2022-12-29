# -*- coding: utf-8 -*-

from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offers"

    price = fields.Float('Price')
    status = fields.Selection(
        string='Status',
        selection=[('accepeted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    property_id = fields.Many2one('estate.property',required=True)
    partner_id = fields.Many2one('res.partner',required=True)