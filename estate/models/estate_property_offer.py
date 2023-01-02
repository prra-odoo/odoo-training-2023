# -*- coding: utf-8 -*-

from odoo import models,fields

class esattePropertyOffer(models.Model):
	_name="estate.property.offer"
	_description="This model defines the estate property offers"

	price=fields.Float("Offer Price")
	status=fields.Selection(
		string="Status",
		selection=[('accepted','Accepted'),('refused','Refused')], copy=False)
	partner_id=fields.Many2one('res.partner',required=True,string="Buyer")
	property_id=fields.Many2one('estate.property',required=True)