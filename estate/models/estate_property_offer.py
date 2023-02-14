# -*- coding: utf-8 -*-
from odoo import fields, models,api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Estate Property Offer Model _description"

    price = fields.Float()
    status = fields.Selection(string="Status",selection=[('accepted',"Accepted"),('refused',"Refused")],copy=False)
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_computed_date_deadline",inverse="_inverse_date_deadline")

    @api.depends("validity","create_date")
    def _computed_date_deadline(self):
        for record in self:
            if(not record.create_date):
                record.create_date = fields.Date.today()
            record.date_deadline = fields.Date.from_string(record.create_date) + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
                record.validity = (record.date_deadline-datetime.date(record.create_date)).days

    def offer_accept(self):
        for offers in self.property_id.offer_ids:
            offers.status = "refused"
        self.status="accepted"
        self.property_id.state="offer_accepted"
        self.property_id.selling_price=self.price
        self.property_id.buyer_id=self.partner_id
        return True
    
    def offer_reject(self):
        self.status="refused"
        return True