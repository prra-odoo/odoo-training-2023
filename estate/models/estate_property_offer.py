# -*- coding: utf-8 -*-
from odoo import models,fields

class Estate_Property_Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

    price = fields.Float(string="Price")
    status = fields.Selection([('accepted','Accepted'),('refused','Refused'),],copy = False, string="Status")
    partner_id = fields.Many2one('res.partner',string = 'Parter',required=True)
    property_id = fields.Many2one('estate.property',string = 'Property',required=True)

    validity = fields.Integer(string="Validity(days)")
    date_deadline = fields.Date(string="Deadline")
    create_date = fields.Date("")

    #validity date

    @api.depends("validity","create_date")
    def _compute_date_deadline(self):
        for record in self:
