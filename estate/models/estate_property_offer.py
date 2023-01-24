# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import timedelta
from datetime import date

class Estate_Property_Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

    price = fields.Float(string="Price")
    status = fields.Selection([('accepted','Accepted'),('refused','Refused'),],copy = False, string="Status")
    partner_id = fields.Many2one('res.partner',string = 'Parter',required=True)
    property_id = fields.Many2one('estate.property',string = 'Property',required=True)
    validity = fields.Integer(string="Validity(days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_dateline",inverse="_inverse_days")
    create_date = fields.Date(default=date.today())
    
# 
    #validity date

    @api.depends("validity")
    def _compute_dateline(self):
        for record in self:
            record.date_deadline = date.today() + timedelta(days=record.validity)

    def _inverse_days(self):
        for record in self:
            record.validity = (record.date_deadline-record.create_date).days
