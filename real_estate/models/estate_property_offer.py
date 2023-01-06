# -*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.tools.date_utils import add
from odoo.exceptions import UserError

class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _order = "price desc"

    price=fields.Float(string='Price')
    status=fields.Selection(string='Status',copy=False, 
                    selection=[('accepted', 'Accepted'),('refused', 'Refused')]
                    )
    partner_id=fields.Many2one("res.partner", required=True)
    property_id=fields.Many2one("estate.property", required=True)
    date_deadline=fields.Date(string="Deadline", compute="_date_deadline", inverse="_inverse_date_deadline")
    validity=fields.Integer(string="Validity(Days)", default=7)
    create_date=fields.Date(string='Create Date', default=fields.Datetime.now())
    property_type_id=fields.Many2one("estate.property.type", related="property_id.property_type_id", string="Property Type", store=True)

    _sql_constraints = [
        ('price', 'CHECK(price >= 0)', 'A Offer price should be positive.')
    ]

    @api.depends("validity",)
    def _date_deadline(self):
        for record in self:
            record.date_deadline = add(fields.Datetime.now(), days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
           day = record.date_deadline - record.create_date
           record.validity = day.days

    def action_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.status"):
            raise UserError("this is error")
        else:
            for record in self:
                record.status='accepted'
                record.property_id.selling_price=record.price
                record.property_id.buyer_id=record.partner_id
 
    def action_refuse(self):
        for record in self:
            record.status='refused'
