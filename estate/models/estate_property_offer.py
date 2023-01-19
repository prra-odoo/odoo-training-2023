# -*- coding: utf-8 -*-

from odoo import models,_,fields,api
from datetime import date
from odoo.tools.date_utils import add
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class estatepropertyoffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers Model"
    _order = "price desc"

    date_deadline = fields.Date(compute="_compute_deadline_date",inverse="_inverse_deadline_date")
    create_date=fields.Date(default=lambda self:fields.Datetime.today())
    price = fields.Float(string="Property Price:")
    validity = fields.Integer(string="Validity in Months",default=7)
    status = fields.Selection(selection=[('accepted','Accepted'),('refuse','Refused')],readonly=True)
    property_type_id = fields.Many2one('estate.property.type',related="property_id.property_type_id", store=True)
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",string="Property",required=True)

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
        for rec in self.search([('status','=','accepted')]):
            if rec.property_id == self.property_id:
                for record in rec.search([('status','=','accepted')]):
                    if record.partner_id != self.partner_id:
                        raise ValidationError(_("cannot accept more than one offer"))
                    else:
                        for rec in self:
                            self.status='refuse'  
        self.status='accepted'
        self.property_id.state='offeraccepted'
        self.property_id.selling_price = self.price
        self.property_id.buyers_id = self.partner_id
            
    def action_refuse(self):
        for record in self:
            record.status = 'refuse'

    @api.model
    def create(self,vals):
        self.env['estate.property'].browse(vals['property_id']).state = 'offerrecieved'
        return super().create(vals)
