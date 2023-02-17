# -*- coding: utf-8 -*-
from odoo import fields, models,api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Estate Property Offer Model _description"
    _sql_constraints = [
        ('price','CHECK(price>0)','Offer Price must be strictly positive')
    ]
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(string="Status",selection=[('accepted',"Accepted"),('refused',"Refused")],copy=False)
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",required=True,ondelete="cascade")
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_computed_date_deadline",inverse="_inverse_date_deadline")
    property_type_id = fields.Many2one(related="property_id.property_type_id",store=True)

    @api.depends("validity","create_date")
    def _computed_date_deadline(self):
        for record in self:
            if(not record.create_date):
                record.create_date = fields.Date.today()
            record.date_deadline = fields.Date.from_string(record.create_date) + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
                if(record.date_deadline > fields.Date.today()):
                    record.validity = (record.date_deadline-datetime.date(record.create_date)).days
                else:
                    record.validity = 0


    def action_accept(self):
        for offers in self.property_id.offer_ids:
            offers.status = "refused"
        self.status="accepted"
        self.property_id.state="offer_accepted"
        self.property_id.selling_price=self.price
        self.property_id.buyer_id=self.partner_id
        return True
    
    def action_reject(self):
        self.status="refused"
        return True