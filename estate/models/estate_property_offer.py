# -*- coding: utf-8 -*-
from odoo import api,fields, models
from dateutil.relativedelta import relativedelta


class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"
    _sql_constraints = [
        ("check_price", "CHECK(price>0)", "An offer price must be strictly positive"),
    ]


    price=fields.Float(string="Price")
    status=fields.Selection([('accepted', 'Accepted'),('refused', 'Refused'),],string="Status",
        copy=False)
    partner_id=fields.Many2one('res.partner',string='Buyer',required=True)
    property_id=fields.Many2one('estate.property',required=True)
    validity=fields.Integer(string="Validity (days)",default="7")
    create_date = fields.Date(default=fields.Date.today())
    # computed field 
    date_deadline=fields.Date(string="Deadline",compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    # compute method
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    # BUTTONS
    def offer_accepted(self):
        for record in self:
            record.status = "accepted"
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
        return True
    def offer_rejected(self):
        for record in self:
            record.status = "refused"
        return True



                
