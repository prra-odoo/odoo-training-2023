# -*- coding: utf-8 -*-
from odoo import fields, models,api,exceptions
from dateutil.relativedelta import relativedelta
from datetime import datetime

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Estate Property Offer Model _description"
    _sql_constraints = [
        ('check_price','CHECK(price>0)','Offer Price must be strictly positive')
    ]
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(string="Status",selection=[('refused',"Refused"),('accepted',"Accepted")],copy=False)
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",required=True,ondelete="cascade")
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_computed_date_deadline",inverse="_inverse_date_deadline")
    property_type_id = fields.Many2one(related="property_id.property_type_id",store=True)
    color = fields.Integer("Color",compute="_compute_color",default=0,readonly=False)

    @api.depends("status")
    def _compute_color(self):
        for record in self:
            if(record.status):
                if(record.status=="accepted"):
                    record.color=10
                else:
                    record.color=1

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
                    if(record.validity<0):
                        record.validity=0
                else:
                    record.validity = 0


    def action_accept(self):
        for record in self:
            for offers in record.property_id.offer_ids:
                offers.status = "refused"
            record.status="accepted"
            record.property_id.state="offer_accepted"
            record.property_id.selling_price=record.price
            record.property_id.buyer_id=record.partner_id
        return True
    
    def action_reject(self):
        for record in self:
            record.status="refused"
        return True
    
    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            best_offer = self.env['estate.property'].browse(vals['property_id']).best_offer
            if(vals['price']<best_offer):
                raise exceptions.UserError("Offer Price cannot be less than %d."%best_offer)
        return super(EstatePropertyOffer,self).create(vals_list)
