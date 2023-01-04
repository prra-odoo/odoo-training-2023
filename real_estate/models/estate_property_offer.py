# -*- coding:utf:8 -*-

from odoo import models, fields, api
from odoo.tools.date_utils import add
from odoo.exceptions import UserError,ValidationError

from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Offer module"
    _order = "price desc"

    price = fields.Float("Price")
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    validity = fields.Integer()
    date_deadline = fields.Date(
        "Date Deadline", compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    create_date = fields.Date(default=fields.Datetime.now(), readonly=True)

    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)',
         'UserError : Enter the Validate Price')
    ]
   
    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = add(
                record.create_date, days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline -
                                   record.create_date).days
    @api.depends("property_id.buyer_id", "property.selling_price", "property_id.state")
    def action_accept(self):
         if self.property_id.selling_price == 0:
            self.property_id.selling_price = self.price
            self.property_id.buyer_id = self.partner_id
            self.status = "accepted"
            self.property_id.state = "sold"
        # for record in self:
        #     if record.status == "accepted":
        #         record.property_id.buyer_id = record.partner_id
        #         record.property_id.selling_price = record.price
        #     record.status = 'accepted'

    def action_refuse(self):
        # for record in self:
            # if record.status == " accepted":
            self.status = 'refused'
            self.property_id.selling_price = 0

   
