# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError , ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer Model"
    _rec_name = "price"
    _order = "price desc"

    price = fields.Float(string='Price')
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate.property')
    validity = fields.Integer(default="7")
    property_type_id = fields.Many2one(related='property_id.property_type_id',store=True)
    date_deadline = fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days = record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days = record.validity)

    def _inverse_date_deadline(self): 
        for record in self:
            if(record.date_deadline > datetime.date(datetime.today())):
                record.validity = (record.date_deadline - record.create_date.date()).days
            

    def action_accept(self):
        for record in self.property_id.offers_id:
            record.status="refused"
            record.property_id.selling_price = self.price
            record.property_id.partner_id = self.partner_id
        self.status = "accepted"
        self.property_id.state = "offer_accepted"


    def action_refuse(self):
        for record in self:
            record.status = "refused"
    
    _sql_constraints = [
        ('check_price','CHECK(price>0)','Offer price must be positive.'),
        ('check_validity', 'CHECK(validity>0)','validity must be greater than 0.')
    ]

    @api.constrains('price')
    def valid_price(self):
        for record in self:
            if record.price < (record.property_id.expected_price * 0.9 ):
                raise ValidationError('Offer price must be greater than 90% of the expected price.')

    @api.constrains('date_deadline')
    def valid_date(self):
        for record in self:
            if record.date_deadline < fields.Date.today():
                raise ValidationError("Enter Valid Date.")