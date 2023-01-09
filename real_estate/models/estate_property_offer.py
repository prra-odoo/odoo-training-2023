# -*- coding: utf-8 -*-

from odoo import models,fields

class estate_property_offer(models.Model):
    _name="estate.property.offer"
    _description="Offers for a property"

    price=fields.Float()
    status=fields.Selection(
        string="Status of the offer",
        selection=[("accepted","Accepted"),("refuse","Refused")],
        copy=False
    )
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("real.estate.properties",required=True)
    