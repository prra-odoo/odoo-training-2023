# -*- coding: utf-8 -*-

from odoo import models, fields

class estateOffer(models.Model):
    _name="estate.property.offer"
    _description = "This is the estate property offer model"
    
    price = fields.Float()
    status = fields.Selection(
        string = "status",
        selection = [('accepted','Accepted'),('refused','Refused')]
    )
    partner_id = fields.Many2one("res.partner",string="Partner id", required=True)
    property_id= fields.Many2one("estate.property",string="Property id",required=True)
    