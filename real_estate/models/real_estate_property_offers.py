from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date
from odoo.exceptions import UserError


class EstatePropertyOffers(models.Model):
    _name = "estate.property.offer"
    _description = "This model will contain estate property all the offers, price, status etc."


    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)

    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date", inverse="_inverse_date")

    @api.depends('validity')
    def _compute_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            record.validity = (record.date_deadline - date.today()).days


    
    @api.depends('status', 'price', 'property_id', 'partner_id')
    def action_confirm(self):
        
        for record in self:
            # id = record.property_id
            # record.status = 'accepted'
            record.property_id.offer_ids.status = 'refused'
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

    def action_reject(self):
        for record in self:
            record.status = 'refused'