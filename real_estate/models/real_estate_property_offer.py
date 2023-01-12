from odoo import api, fields, models
from datetime import timedelta
import datetime
 

class RealEstatePropertyOffer(models.Model):
    _name = "real.estate.property.offer"
    _description = "Property Offers"

    price = fields.Float(required=True)
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused'),], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("real.estate.property", string="Property Name", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline_date", inverse="_inverse_deadline_date", store=True)

    _sql_constraints = [('check_offer_price', 'CHECK(price > 0)', 'The price of an proerty should be greater than 0')]
    
    @api.depends('create_date', 'validity')
    def _compute_deadline_date(self):
        for record in self:
            for record in self:
                if record.create_date:
                    record.date_deadline=record.create_date + timedelta(days=record.validity)
                else:
                    record.date_deadline = datetime.date.today() + timedelta(days=record.validity)
            #     print(record.property_id.create_date)
            # print(record.validity)
            # record.date_deadline = (record.property_id.create_date + timedelta(days=record.validity)).date()

    def _inverse_deadline_date(self):
        for record in self:
            record.validity = (record.date_deadline -
                               record.create_date.date()).days

    def action_confirm(self):
        for record in self:
            record.property_id.offer_ids.status = "refused"
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

    def action_cancel(self):
        for record in self:
            record.status = 'refused'
