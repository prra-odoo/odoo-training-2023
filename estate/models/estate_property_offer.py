# -*- coding: utf-8 -*-
from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Estate Property Offer Model _description"

    price = fields.Float()
    status = fields.Selection(string="Status",selection=[('accepted',"Accepted"),('refused',"Refused")],copy=False)
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",required=True)
