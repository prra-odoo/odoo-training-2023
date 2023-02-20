# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class estatePropertyoffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is regarding the real_estate"
    _order = "price desc"

    price = fields.Float(string='Price')
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', string='Partner_id')
    property_id = fields.Many2one(
        'real.estate', string='Property Id', required=True)
    validity = fields.Integer(string='Validity(days)', default='7')
    date_deadline = fields.Date(
        string='Deadline', compute="_date_deadline", inverse="_inverse_date_deadline")
    create_date = fields.Date(
        default=fields.Datetime.now(), string='Create Date')
    property_type_id = fields.Many2one(
        "estate.property.type", related="property_id.property_type_id", string="Property Type", store=True)

    @api.depends("validity")
    def _date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + \
                relativedelta(days=+ record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            day = record.date_deadline - record.create_date
            record.validity = day.days

    def offer_accepted(self):
        for record in self:
            if "accepted" in self.mapped("property_id.offer_ids.status"):
                raise UserError("Its an Error")
            else:
                for record in self:
                    record.status = "accepted"
                    record.property_id.selling_price = record.price
                    record.property_id.buyer_id = record.partner_id
                    record.property_id.state = 'offer_accepted'

    def offer_refused(self):
        for record in self:
            record.status = "refused"

    _sql_constraints = [
        ('price', 'CHECK(price>=0)', 'Offer Price should be positive')]

    @api.model
    def create(self, vals):
        max_offer = 0
        if vals.get("property_id") and vals.get("price"):
            rec = self.env['real.estate'].browse(vals['property_id'])
            if rec.offer_ids:
                max_offer = max(rec.mapped("offer_ids.price"))
                if max_offer > vals['price']:
                    raise UserError(f'Offer must be higher than {max_offer}')
            rec.state = 'offer_received'
        return super().create(vals)
