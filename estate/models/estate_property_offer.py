# -*- coding: utf-8 -*-

from odoo import models,_,fields,api
from datetime import date
from odoo.tools.date_utils import add
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from odoo.tools import float_is_zero,float_compare


class estatepropertyoffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers Model"
    _order = "price asc"

    date_deadline = fields.Date(compute="_compute_deadline_date",inverse="_inverse_deadline_date")
    create_date=fields.Date(default=lambda self:fields.Datetime.today())
    price = fields.Float(string="Property Price:")
    validity = fields.Integer(string="Validity in Months",default=7)
    status = fields.Selection(selection=[('accepted','Accepted'),('refuse','Refused')],readonly=True)
    property_type_id = fields.Many2one('estate.property.type',related="property_id.property_type_id", store=True)
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",string="Property Name:",required=True)

    _sql_constraints=[
        ('check_Offer_price','CHECK(price >= 0)','Offer Price cannot be negative')
    ]

    @api.depends('validity','date_deadline')
    def _compute_deadline_date(self):
        for record in self:
            record.date_deadline= record.create_date + relativedelta(days=record.validity)

    def _inverse_deadline_date(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    @api.depends('status','property_id.status')
    def action_accept(self):
        if 'accepted' in self.mapped("property_id.offer_ids.status"):
            raise ValidationError("Cannot Accept Offers from Multiple Properties!!")
        else:
            for record in self:
                record.status = 'accepted'
                record.property_id.selling_price = record.price
                record.property_id.buyers_id = record.partner_id
                record.property_id.state = 'offeraccepted'
        offers = self.env['estate.property.offer'].search([])
        offer_status = offers.mapped('property_id.offer_ids.status')
        for off in offers:
            if off.status != 'accepted':
                off.status='refuse'
        return True
            
    def action_refuse(self):
        for record in self:
            record.status = 'refuse'

    @api.model
    def create(self,vals):
        rec = self.env['estate.property'].browse(vals['property_id'])
        if rec.offer_ids:
            maxPrice = max(rec.mapped('offer_ids.price'))
            if float_compare(vals['price'],maxPrice,precision_rounding = 0.01) <=0:
                raise ValidationError("Offer must be higer than current offers")
        rec.state = 'offerrecieved'
        return super().create(vals)
