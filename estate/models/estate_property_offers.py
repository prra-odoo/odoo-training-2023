# -- coding: utf-8 --
from odoo import models, fields

class EstatePropertyOffers(models.Model):
    _name = "estate.property.offers"
    _description = "estate property offer Model"

    price = fields.Float(string='Price')
    status = fields.Selection(
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False
    )
    buyer_id=fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property')