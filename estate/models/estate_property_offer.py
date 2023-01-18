# -*- coding: utf-8 -*-
from odoo import fields,models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is Estate Property offer"
    # Table fields
    price = fields.Float(string="Price")
    status = fields.Selection(
        string="Status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False,
    )
    # Relational Fields
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)