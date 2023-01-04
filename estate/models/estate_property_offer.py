# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.date_utils import add


class EstatePropertyType(models.Model):
    _name = "estate.property.offer"
    _description = "Types of the different Real Estate Property"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one(
        "res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property Id")
    validity = fields.Integer(string="Validity", default=3)
    date_deadline = fields.Date(
        string="Deadline Date", compute="_date_deadline", inverse="_inverse_date_deadline")
    create_date = fields.Date(
        default=fields.Datetime.now(), string="Create Date", readonly=True)
        

    _sql_constraints = [
        ("check_price_is_positive", "CHECK(price > 0)", "Price Should Be Positive")
    ]

    # Compute Function
    @api.depends("validity", "create_date")
    def _date_deadline(self):
        self.date_deadline = add(self.create_date, days=self.validity)

    def _inverse_date_deadline(self):
        if self.date_deadline:
            self.validity = (self.date_deadline - self.create_date).days

    # Buttons
    @api.depends("property_id.buyer_id", "property.selling_price", "property_id.state")
    def offer_accepted_action(self):
        if self.property_id.selling_price == 0:
            self.property_id.selling_price = self.price
            self.property_id.buyer_id = self.partner_id
            self.status = "accepted"
            self.property_id.state = "offer_accepted"

    def offer_rejected_action(self):
        self.status = "refused"
        self.property_id.selling_price = 0
        self.property_id.state = "new"
