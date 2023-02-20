# -*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.tools.date_utils import add
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
from odoo.tools import float_compare

class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _order = "price desc"

    price = fields.Float(string='Price')
    status = fields.Selection(string='Status',copy=False, 
                    selection=[('accepted', 'Accepted'),('refused', 'Refused')]
                    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    date_deadline = fields.Date(string="Deadline", compute="_date_deadline", inverse="_inverse_date_deadline")
    validity = fields.Integer(string="Validity(Days)", default=7)
    create_date = fields.Date(string='Create Date', default=fields.Datetime.now())
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", string="Property Type", store=True)

    _sql_constraints = [
        ('price', 'CHECK(price >= 0)', 'A Offer price should be positive.')
    ]

    @api.depends('validity')
    def _date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days =+ record.validity)

    def _inverse_date_deadline(self):
        for record in self:
           record.validity = (record.date_deadline - record.create_date).days

    @api.depends('property.selling_price', 'property_id.buyer_id', 'property_id.state', 'property_id.offer_ids')
    def action_accept(self):
        domain = ['property_id.offer_ids', "=", self.id]
        records = self.env['estate.property.offer'].search([domain])
        for record in self:
            record.status='accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = 'offer_accepted'
        
        for record in records:
            if record.status!='accepted':
                record.status='refused'              

    def action_refuse(self):
        for record in self:
            record.status='refused'

    @api.model
    def create(self, vals):
        domain = ['property_id', '=', vals['property_id']]
        result = self.env['estate.property.offer'].search([domain]).mapped('price')
        for record in result:
            if vals['price'] < record:
                raise UserError("Increasing Your Amount")
        self.env['estate.property'].browse(vals['property_id']).state = "offer_received"
        return super().create(vals)
        