# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Estate Property Offers"

    price=fields.Float('Price')
    status=fields.Selection(string="offer status", selection=[('accepted','Accepted'),('refused','Refused')], copy=False)
    partner_id=fields.Many2one('res.partner', required=True)
    property_id=fields.Many2one('estate.properties', required=True)