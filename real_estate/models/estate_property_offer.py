# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = " A property offer is an amount a potential buyer offers to the seller."
    
    price = fields.Float(string="Price")
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'), ('refused','Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(string="Validity (days)", default=7, inverse="_inverse_validity_change")
    date_deadline = fields.Date(string="Deadline", inverse="_inverse_deadline_date")
    
    # Method Decorators

    @api.depends('')
    def _inverse_validity_change(self):
        for record in self:
            record.date_deadline = record.validity + relativedelta()
    
    @api.depends('')
    def _inverse_deadline_date(self):
        for record in self:
            pass