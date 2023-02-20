# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,models,fields
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Estate Property Offers"
    _order="price desc"

    price=fields.Float('Price')
    status=fields.Selection(string="offer status", selection=[('accepted','Accepted'),('refused','Refused')], copy=False)
    partner_id=fields.Many2one('res.partner', required=True)
    property_id=fields.Many2one('estate.properties', required=True)
    validity=fields.Integer('Validity',default=7)
    date_deadline=fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    property_type_id=fields.Many2one(related='property_id.type_id' , store=True)

    _sql_constraints = [
        ('check_price', 'check(price >= 0)', "Offer price cannot be negative.")
    ]

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline=record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Datetime.now() + relativedelta(days=record.validity)  

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days

    def action_accept(self):
        for record in self:
            record.property_id.offer_ids.status='refused'
            record.status = "accepted"
            record.property_id.selling_price=record.price
            record.property_id.buyer_id=record.partner_id

    def action_refused(self):
        for record in self:
            record.status = "refused"

    @api.model
    def create(self,vals):
        property_id=self.env['estate.properties'].browse(vals['property_id'])
        property_id.state='offer_received'
        if vals['price']<property_id.best_offer:
            raise UserError(("New offer cannot be less than the previous offer"))
        return super().create(vals)
    