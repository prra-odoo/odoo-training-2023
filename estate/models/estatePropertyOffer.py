# -- coding: utf-8 --

from odoo import fields,models

class estateProperty(models.Model):
    _name = "estate.property.offer"
    _description="model description"

    price=fields.Float(string="Price")
    status=fields.Selection( string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])

    partner_id=fields.Many2one('res.partner',required=True)
    name=fields.Many2one('estate.property')