# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offers"

    price = fields.Float('Price')
    status = fields.Selection(
        string='Status',
        selection=[('accepeted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    property_id = fields.Many2one('estate.property',required=True)
    partner_id = fields.Many2one('res.partner',required=True)
    # validity = fields.Integer('Validity',default='7')
    # date_deadline = fields.Date(compute='_compute_date', inverse='_inverse_date')
    # create_date = fields.Date('create date',default=lambda self:fields.Datetime.now())
    # @api.depends('validity', 'create_date')
    # def _compute_date(self):
    #     for record in self:
    #         record.date_deadline = sum(record.create_date, record.validity)

    # def _inverse_date(self):
    #     for record in self:
    #         record.validity = record.date_deadline - record.create_date