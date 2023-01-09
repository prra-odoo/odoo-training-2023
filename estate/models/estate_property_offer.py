# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class EstateModel(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _inherit = "mail.thread"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused'),], copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", string="Property Type", store=True)
    validity = fields.Integer(default=7)
    create_date = fields.Date(default=lambda self: fields.datetime.now(), readonly=True)
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")

    _sql_constraints = [
        ('check_offer_price', 'CHECK(price >= 0)',
         'The offer price should be positive')
    ]

    @api.depends("validity", "create_date")
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days = record.validity)


    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days

    def action_accept(self):
        for record in self.search([('status', '=', 'accepted')]):
            if record.property_id == self.property_id:
                for rec in record.search([('status', '=', 'accepted')]):
                    if rec.partner_id != record.partner_id:
                        raise UserError("one offer already accepted")
                    else:
                        rec.status = "refused"
        self.status = "accepted"
        self.property_id.buyers_id = self.partner_id
        self.property_id.selling_price = self.price
        self.property_id.state = "offer_accepted"

    def action_refuse(self):
        for record in self:
            record.status = "refused"

