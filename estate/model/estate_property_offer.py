# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.date_utils import add
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare
from dateutil.relativedelta import relativedelta

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

    partner_id = fields.Many2one('res.partner','Buyer',required=True)
    property_type_id = fields.Many2one('estate.property.type',related='property_id.property_type_id',string='Property type', store=True)
        # equivalent to -->
        # @api.depends("property_id.property_type_id")
        # def _compute_description(self):
        # for record in self:
        #     record.property_type_id = property_id.property_type_id

    validity = fields.Integer('Validity(days)',default='7')
    date_deadline = fields.Date(compute='_compute_date', inverse='_inverse_date')
    create_date = fields.Date('Date availability',default=fields.Datetime.now())

    #create method
    @api.model
    def create(self, vals):
        property_id = self.env['estate.property'].browse(vals['property_id'])
        if float_compare(vals.get('price'),max(property_id.offer_ids.mapped('price'), default=0),precision_digits=2) <= 0:
            raise UserError('The new offer must be greater than existing one')
        property_id.state = 'offer_received'
        return super().create(vals)

    #computing date deadline
    @api.depends('validity')
    def _compute_date(self):
        for record in self:
            record.date_deadline = add(record.create_date,days=record.validity)
    
    #computing validity - inverse
    @api.depends('validity')
    def _inverse_date(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    # accepted button action
    def action_accepted(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError("An offer is already been accepted.")
            record.status = 'accepted'
            record.property_id.state = 'offer_accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
        return True

    # refuse button action
    def action_refused(self):
        for record in self:
            record.status = 'refused'
        return True
    
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'The offer price must be stricly positive.'),
    ]

