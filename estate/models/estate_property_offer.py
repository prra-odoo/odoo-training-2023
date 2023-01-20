# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"

    price = fields.Float()
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

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=+record.validity)
    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days

    def accept_offer(self):
            for record in self:
                # record.status='refused'
                self.status ='accepted'
                self.property_id.selling_price=self.price
            return True
    
    def reject_offer(self):
            self.status ='refused'
            return True
