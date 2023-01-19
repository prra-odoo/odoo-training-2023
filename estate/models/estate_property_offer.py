# -*- coding: utf-8 -*-
from odoo import fields, models

class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"

    price=fields.Float(string="Price")
    status=fields.Selection([('accepted', 'Accepted'),('refused', 'Refused'),],string="Status",
        copy=False)
    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('estate.property',required=True)
    validity =fields.Integer(string="Validity (days)",default="7")
    # computed field 
