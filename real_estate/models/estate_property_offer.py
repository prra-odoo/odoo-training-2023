# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = " A property offer is an amount a potential buyer offers to the seller."
    
    price = fields.Float(string="Price")
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'), ('refused','Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    # Method Decorators

    @api.depends("validity", "date_deadline", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            # print(record.property_id.name)
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Datetime.now() + relativedelta(days=record.validity)
                
    @api.depends("date_deadline", "create_date")    
    def _inverse_date_deadline(self):
        for record in self:
            print(record.date_deadline)
            print(record.create_date)
            record.validity = (record.date_deadline - record.create_date.date()).days