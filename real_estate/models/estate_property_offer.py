# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import ValidationError

class estate_property_offers(models.Model):
    _name = 'estate.property.offer'
    _description = "Estate Property Offers"

    price = fields.Float('Price',required=True,default=0)
    status = fields.Selection(
            string='Status',copy=False,
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
            self.status = 'accepted'
            value = ((self.property_id.expected_price) * 90)/100
            if self.price < value:
                    raise ValidationError("selling price must be 90 percentage of expected_price")
            else:
                    self.property_id.selling_price = self.price
                    self.property_id.buyer = self.partner_id    

    def action_refuse(self):
            self.status = 'refused'
            self.property_id.selling_price = 0
            
