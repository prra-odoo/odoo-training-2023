# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer is the amount of a potential buyer offers to the seller."
    _order = "price desc"

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
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", store=True)

    _sql_constraints = [
        ('check_offer_price', 'CHECK(price>=0)', 'Offer price must be Strictly Positive!')
    ]

    @api.depends('validity', 'date_deadline', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    def action_offer_rejected(self):
        for record in self:
            record.status = 'refused'
            if record.status == 'accepted':
                record.property_id.selling_price = 0
        return True

    def action_offer_accepted(self):
        if 'accepted' in self.mapped("property_id.offer_ids.status"):
            raise UserError("Cannot Accept Offers from Multiple Properties!!")
        else:
            for record in self:
                record.status = 'accepted'
                record.property_id.selling_price = record.price
                record.property_id.buyer_id = record.partner_id
                record.property_id.state = 'offer_accepted'
        return True

    # def create(self, vals):
        # for val in vals:
        # how to get value of current price???????????
            # self.env['estate.property'].browse(vals['property_id.offer_ids.price'])
