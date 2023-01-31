# -*- coding: utf-8 -*-
from odoo import api,fields, models
from dateutil.relativedelta import relativedelta


class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"
    _order = "price desc"
    _sql_constraints = [
        ("check_price", "CHECK(price >0)", "An offer price must be strictly positive"),
    ]


    price=fields.Float(string="Price")
    status=fields.Selection([('accepted', 'Accepted'),('refused', 'Refused'),],string="Status",
        copy=False,default=False)
    partner_id=fields.Many2one('res.partner',string='Buyer',required=True)
    property_id=fields.Many2one('estate.property',required=True)
    validity=fields.Integer(string="Validity (days)",default="7")
    create_date = fields.Date(default=fields.Date.today())
    # Related field
    property_offers_id = fields.Many2one(related='property_id.property_type_id',store=True)
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
            for record in self.property_id.offer_ids:
                record.status = "refused"
            self.status = "accepted"
            self.property_id.buyer_id = self.partner_id
            self.property_id.selling_price = self.price
            self.property_id.state="offer_accepted"
        return True
    def offer_rejected(self):
        for record in self:
            record.status = "refused"
        return True



                
