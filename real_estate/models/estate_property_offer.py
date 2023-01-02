# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.date_utils import add, subtract

class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer is the amount of a potential buyer offers to the seller."

    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = add(fields.Datetime.now(), days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = subtract(record.date_deadline, fields.Datetime.now())
