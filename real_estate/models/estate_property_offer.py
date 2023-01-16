# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import ValidationError,UserError
from odoo.tools import float_is_zero,float_compare

class estate_property_offers(models.Model):
    _name = 'estate.property.offer'
    _description = "Estate Property Offers"
    _order = "price desc"

    price = fields.Float('Price',required=True,default=0)
    states = fields.Selection(
            string='States',copy=False,
            selection=[('refused','refused'),('accepted','accepted')])
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer('validity',default=7)
    date_deadline = fields.Date('date_deadline',default=datetime.today(), compute="_compute_dead_line",inverse="_inverse_date_deadline")


    _sql_constraints = [('check_offer_price','CHECK(price >= 0)','A property offer price must be strictly positive.')]




    @api.depends("validity")
    def _compute_dead_line(self):
            for record in self:
                    if record.create_date:
                            record.date_deadline = (((record.create_date).date()) + relativedelta(days=+record.validity))
                            
                    else:
                            record.date_deadline = ((datetime.today()) + relativedelta(days=self.validity))

    def _inverse_date_deadline(self):
            for record in self:
                    if record.date_deadline:
                            d1 = (record.date_deadline)
                            d2 = (record.create_date).date()
                            record.validity = (d1-d2).days

    def action_accepted(self):
            for record in self:
                    record.property_id.offer_ids.states='refused'
                    record.states='accepted'

                    if(float_compare(record.price,record.property_id.expected_price * 0.9,precision_rounding=0.01)<0):
                            raise UserError("Selling Price must 90percent of the expected price")
                    else:
                            record.property_id.selling_price = record.price
                            record.property_id.buyer = record.partner_id 
                            record.property_id.status = 'offer Accepted'
       

    def action_refuse(self):
            self.states = 'refused'
            self.property_id.selling_price = 0
            
