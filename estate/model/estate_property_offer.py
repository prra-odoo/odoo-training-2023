# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, time
from odoo.exceptions import UserError
from odoo.tools.date_utils import add


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
    property_type_id = fields.Many2one('estate.property.type',related='property_id.property_type_id',string='Property type', store=True)
        # equivalent to -->
        # @api.depends("property_id.property_type_id")
        # def _compute_description(self):
        # for record in self:
        #     record.property_type_id = property_id.property_type_id

    validity = fields.Integer('Validity(days)',default='7')
    date_deadline = fields.Date(compute='_compute_date', inverse='_inverse_date')
    create_date = fields.Date('Date availability',default=fields.Datetime.now())

    @api.model
    def create(self, vals_list):
        for vals in vals_list:
            self.env['estate.property'].browse(vals['property_id'])
            vals.price = '1000'
        return super().create(vals)

    # @api.model
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if 'price' in vals:
    #             property_id = self.env['estate.property.offer'].browse(vals['property_id'])
    #             property_id.state = 'offer_received'
    #     return super(EstatePropertyOffer, self).create(vals)

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
            if "accepted" in self.mapped("property_id.offer_ids.status"):
                raise UserError("An offer is already been accepted.")
            record.status = 'accepted'
            record.property_id.state = 'offer_accepted'
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