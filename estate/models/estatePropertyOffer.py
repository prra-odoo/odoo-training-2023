# -- coding: utf-8 --

from odoo import fields,models,api
from . import estateProperty
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
import datetime

TODAY = datetime.date.today()

class estateProperty(models.Model):
    _name = "estate.property.offer"
    _description="model description"
    _order="price desc"

    price=fields.Float(string="Price")

    @api.constrains('price')
    def _check_date_end(self):
        for record in self:
            if record.price<max(record.property_id.offer_ids.mapped("price"),default=0):
                raise ValidationError("Please place a greater offer")


    status=fields.Selection( string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])

    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('estate.property')


    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_deadline", inverse="_compute_days")

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            record.date_deadline=TODAY+relativedelta(days=record.validity)


    def _compute_days(self):
        # for record in self:
        #     record.validity=record.date_deadline-record.create_date.date
        pass

    def accept_offer(self):
        for record in self:            
            record.status='accepted'
            record.property_id.selling_price=record.price
            record.property_id.state='offer_accepted'

            for records in self.property_id.offer_ids:
                if records != self:
                    records.status='refused'


    def reject_offer(self):
        for record in self:
            record.status='refused'

        
