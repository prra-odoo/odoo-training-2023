# -*- coding: utf-8 -*-

from odoo import models, fields

class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer is the amount of a potential buyer offers to the seller."

    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
