# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer Model"
    _rec_name = "price"

    price = fields.Float(string='Price')
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    validity = fields.Integer(default="7")
    date_deadline = fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days = record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days = record.validity)

    def _inverse_date_deadline(self): 
        for record in self:
            if(record.date_deadline > datetime.date(datetime.today())):
                record.validity = (record.date_deadline - record.create_date.date()).days
            else:
                record.validity = 0

    def action_accept(self):
        for record in self.property_id.offers_id:
            if record.status == "accepted":
                raise UserError("Alredy one offer accepted.")
            else:
                self.status = "accepted"
                self.property_id.selling_price = self.price
        return True


    def action_refuse(self):
        for record in self.property_id.offers_id:
            if self.status == "accepted":
                raise UserError("Alredy offer accepted.")
            else:
                self.status = "refused"
        return True