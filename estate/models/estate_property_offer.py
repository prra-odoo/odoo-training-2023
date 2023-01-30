# -*- coding: utf-8 -*-

from odoo import fields, models, api,exceptions
from datetime import date
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"
    _order = "price desc"

    price = fields.Float(default="1")
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline", string="Deadline")
    validity = fields.Integer(string="Validity",default="7")
    create_date = fields.Date(default=date.today())
    property_type_id = fields.Many2one(related="property_id.property_type_id")

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=+record.validity)
    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days

    def accept_offer(self):
        for record in self:
                for records in self.property_id.offer_ids:
                    if records.status == 'accepted':
                        records.status = 'refused'
                self.status ='accepted'
                self.property_id.selling_price=self.price
                self.property_id.state="offer_accepted"
                self.property_id.buyer_id = record.partner_id
        return True
    
    def reject_offer(self):
        self.status ='refused'
        return True

    _sql_constraints = [
            ('check_offerprice', 'CHECK(price > 0)','The offerprice must be positive.'),
        ]
    @api.constrains('price')
    def _adding_best_new_offer(self):
        for record in self:
            if record.price < record.property_id.best_offer:
                raise exceptions.ValidationError("The New offer should be better than the current best offer")
