# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare

class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer is the amount of a potential buyer offers to the seller."
    _order = "price desc"

    # Fields
    price = fields.Float(required=True)
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    validity = fields.Integer(default=7)
    create_date = fields.Date(default=fields.Datetime.now(), readonly=True, copy=False)

    # Relational Fields
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    property_type_id = fields.Many2one('estate.property.type', related="property_id.property_type_id", store=True)

    # Computed Fields
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    # SQL Constraints
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price>=0)', 'Offer price must be Strictly Positive!')
    ]

    # Compute Methods
    @api.depends('validity', 'date_deadline', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    # Actions
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
        offers = self.env['estate.property.offer'].search([])
        offer_status = offers.mapped('property_id.offer_ids.status')
        for off in offers:
            if off.status != 'accepted':
                off.status='refused'
        return True

         # print(list(self.mapped('property_id.offer_ids.status')))
        # offers = self.env['estate.property.offer'].search([('property_id.offer_ids.status', '=', False)])
        # for off in offers:
        #     print(off.status)
        #     if off.status != 'accepted':
        #         off.status = 'refused'

    # Create Method
    @api.model
    def create(self, vals):
        records = self.env['estate.property'].browse(vals['property_id'])
        if records.offer_ids:
            maxPrice = max(records.mapped('offer_ids.price'))
            if float_compare(vals['price'], maxPrice, precision_rounding=0.01) <= 0:
                raise UserError(("Offer Price must be higher than", maxPrice))
        
        records.state = 'offer_received'
        return super().create(vals)
