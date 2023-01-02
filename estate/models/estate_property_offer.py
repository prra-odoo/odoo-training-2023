# -*- coding: utf-8 -*-

from odoo import models,fields

class estatepropertyoffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers Model"

    price = fields.Float(string="Property Price:")
    status = fields.Selection(selection=[('accepted','Accepted'),('refuse','Refused')])
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",string="Property",required=True)