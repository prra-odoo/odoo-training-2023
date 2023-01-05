# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, time
from odoo.exceptions import UserError
from odoo.tools.date_utils import add,subtract

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offers"
    _order = "price desc"

    price = fields.Float('Price')
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    property_id = fields.Many2one('estate.property',required=True)
    partner_id = fields.Many2one('res.partner',required=True)

    validity = fields.Integer('Validity',default='7')
    date_deadline = fields.Date(compute='_compute_date', inverse='_inverse_date')
    create_date = fields.Date('Date availability',default=fields.Datetime.now())

    @api.depends('validity')
    def _compute_date(self):
        for record in self:
            record.date_deadline = add(record.create_date,days=record.validity)

    def _inverse_date(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    #         @api.depends('validity')
    #          def _inverse_validity(self):
    #           for record in self:
    #               record.date_deadline = record.date_availability + relativedelta(days =+ record.validity)
    
    def action_accepted(self):
        for record in self:
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
        return True

    def action_refused(self):
        for record in self:
            record.status = 'refused'
        return True
    
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'The offer price must be stricly positive.'),
    ]