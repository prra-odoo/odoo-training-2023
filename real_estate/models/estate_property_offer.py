# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class estate_property_offers(models.Model):
    _name = 'estate.property.offer'
    _description = "Estate Property Offers"

    price = fields.Float('Price',required=True)
    status = fields.Selection(
            string='Status',copy=False,
            selection=[('refused','refused'),('accepted','accepted')])
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer('validity',default=7)
    date_deadline = fields.Date('date_deadline',default=datetime.today(), compute="_compute_dead_line",inverse="_inverse_date_deadline")



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