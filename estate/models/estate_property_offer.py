# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import timedelta,date
from odoo.exceptions import UserError, ValidationError

class Estate_Property_Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The offer price must be strictly positive"), 
    ]
    _order = "price desc"


    price = fields.Float(string="Price")
    status = fields.Selection([('accepted','Accepted'),('refused','Refused'),],copy = False, string="Status")
    partner_id = fields.Many2one('res.partner',string = 'Partner',required=True)
    property_id = fields.Many2one('estate.property',string = 'Property',required=True)
    property_type_id = fields.Many2one(related="property_id.property_type_id")

    #inverse fields records
    validity = fields.Integer(string="Validity(days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_dateline",inverse="_inverse_days")
    create_date = fields.Date(default=date.today())
 
    #validity date [inverse field]
    #A compute method sets the field 
    @api.depends("validity")
    def _compute_dateline(self):
        for record in self:
            record.date_deadline = date.today() + timedelta(days=record.validity)

    #An inverse method sets the field’s dependencies
    def _inverse_days(self):
        for record in self:
            record.validity = (record.date_deadline-record.create_date).days

    #buttons for accept and refuse the offer
    def action_accept(self):
        for record in self:
            record.status="accepted"
            record.property_id.selling_price= record.price
            record.property_id.buyer_id= record.partner_id
            record.property_id.state='offer_accepted'
        return True    

    def action_refuse(self):
        for record in self:
            record.status="refused"
        return True

    
    @api.model
    def create(self, vals):
        property = self.env['estate.property'].browse(vals['property_id'])
        if vals['price'] < property.best_price:
            raise ValidationError("Please place a greater offer")
        property.state = 'offer_received'   
        return super().create(vals)
                   