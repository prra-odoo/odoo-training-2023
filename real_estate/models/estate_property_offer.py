# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = " A property offer is an amount a potential buyer offers to the seller."
    
    price = fields.Float(string="Price")
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'), ('refused','Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    _sql_constraints = [
        ('best_price_positive', 'check (price > 0)', "The offer price must be strictly positive.")
    ]
    
    # Functions
    
    def action_accept_btn(self):
        for record in self:
            record.property_id.offer_ids.status = 'refused' # First, This will refuse all the available offers
            record.status = 'accepted' # Then, This will accept offer where user clicked.
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
        return True
    
    def action_refuse_btn(self):
        for record in self:
            record.status = 'refused'
        return True
    
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