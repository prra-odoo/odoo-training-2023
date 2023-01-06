# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


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
    property_type_id = fields.Many2one(
        'estate.property.type', related = 'property_id.property_type_id',string="property Type")

    _sql_constraints = [
        ("check_price_is_positive", "CHECK(price > 0)", "Price Should Be Positive")
    ]

    # Compute Function
    @api.depends("validity", "create_date")
    def _date_deadline(self):
        for rec in self:
            rec.date_deadline = rec.create_date + relativedelta(days =+ rec.validity)

    def _inverse_date_deadline(self):
        for rec in self:
            if rec.date_deadline:
                rec.validity = (rec.date_deadline - rec.create_date).days

    # Buttons
    @api.depends("property_id.buyer_id", "property.selling_price", "property_id.state")
    def offer_accepted_action(self):
        for rec in self:
            if rec.property_id.selling_price == 0:
                rec.property_id.selling_price = rec.price
                rec.property_id.buyer_id = rec.partner_id
                rec.status = "accepted"
                rec.property_id.state = "offer_accepted"

    def offer_rejected_action(self):
        for rec in self:
            rec.status = "refused"
            rec.property_id.selling_price = 0
            rec.property_id.state = "new"

    # @api.model
    # def create(self, vals):
    #     for rec in self:
    #         print("hellllo")
    #         print(rec.price)
    #         if not (rec.price > vals['price']) :
    #             raise UserError("Not")
    #     return super(EstatePropertyType, self).create(vals)
