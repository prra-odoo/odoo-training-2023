# -*- coding: utf-8 -*-
from odoo import api,fields, models
from dateutil.relativedelta import relativedelta


class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"

    price=fields.Float(string="Price")
    status=fields.Selection([('accepted', 'Accepted'),('refused', 'Refused'),],string="Status",
        copy=False)
    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('estate.property',required=True)
    validity=fields.Integer(string="Validity (days)",default="7")
    # computed field 
    date_deadline=fields.Date(string="Deadline",compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    # compute method
    # @api.depends("create_date","validity")
    # def _compute_date_deadline(self):
    #     for record in self:
    #         record.date_deadline.date = record.create_date.date() + record.validity.days()

    # def _inverse_date_deadline(self):
    #     for record in self:
    #         record.validity.days = (record.date_deadline - record.create_Date.date()).days
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days
