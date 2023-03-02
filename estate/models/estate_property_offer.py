# -*- coding: utf-8 -*-
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _order = "price desc"

    _sql_constraints = [
        ('check_offer_price','CHECK(price > 0)','The offer price must be strictly positive.'),
        ('check_validity_days','CHECK(validity > 0)','Validity must be positive.')
    ]

    price = fields.Float()
    status = fields.Selection(
        selection = [
            ('accepted', 'Accepted'),
            ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    validity = fields.Integer(default=7)
    deadline_date = fields.Date(compute='_compute_deadline_date', inverse='_inverse_deadline_date')
    property_id = fields.Many2one('estate.property')
    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)

    @api.depends('create_date', 'validity')
    def _compute_deadline_date(self):
        for record in self:
            if(record.create_date):
                record.deadline_date = record.create_date + relativedelta(days=record.validity)
            else:
                record.deadline_date = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_deadline_date(self):
        for record in self:
            if(record.deadline_date > record.create_date.date()):
                record.validity = (record.deadline_date - record.create_date.date()).days

    def action_accept_offer(self):
        for record in self.property_id.offer_ids:
            record.status = 'refused'
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id
        self.status = 'accepted'
        self.property_id.state = 'offer_accepted'
        return True
    
    def action_cancel_offer(self):
        self.status = 'refused'
        self.property_id.buyer_id = None
        return True

    @api.model
    def create(self, vals):
        prop_record = self.env['estate.property'].browse(vals['property_id'])
        if(vals['price'] <= prop_record.best_price):
            raise UserError("Offer price is shouldn't lower than %d" %prop_record.best_price)
        return super(EstatePropertyOffer,self).create(vals)

