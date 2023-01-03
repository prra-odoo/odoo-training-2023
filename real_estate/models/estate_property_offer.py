# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.date_utils import add
from odoo.exceptions import UserError

class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer is the amount of a potential buyer offers to the seller."

    price = fields.Float(required=True)
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    create_date = fields.Date(default=fields.Datetime.now(), readonly=True, copy=False)

    @api.depends('validity', 'date_deadline', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = add(record.create_date, days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days

    def action_offer_accepted(self):
        for record in self:
            record.status = 'accepted'
        return True
    
    def action_offer_rejected(self):
        for record in self:
            record.status = 'refused'
        return True
