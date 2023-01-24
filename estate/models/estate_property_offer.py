# -*- coding: utf-8 -*-
from odoo import api,fields,models
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is Estate Property offer"
    # Table fields
    price = fields.Float(string="Price")
    status = fields.Selection(
        string="Status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False,
    )
    validity = fields.Integer(string="Validity (days)",default=7)
    date_deadline = fields.Date(string="Deadline",compute="_compute_deadline",inverse="_inverse_date_deadline")
    # Relational Fields
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)

    @api.depends("create_date","validity",)
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
                # breakpoint()
            else:
                record.date_deadline = fields.datetime.now() + relativedelta(days=record.validity)    
            
    # @api.depends("date_deadline","create_date")
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days
            
    def  action_confirm(self):
        for record in self:
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.status = "offer_accepted"
            record.status = 'accepted'
        return True

    def action_cancel(self):
        for record in self:
            record.status = 'refused'
        return True

    