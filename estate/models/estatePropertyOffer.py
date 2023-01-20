# -- coding: utf-8 --

from odoo import fields,models,api
from . import estateProperty
from dateutil.relativedelta import relativedelta
import datetime

TODAY = datetime.date.today()

class estateProperty(models.Model):
    _name = "estate.property.offer"
    _description="model description"

    price=fields.Float(string="Price")
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
        for record in self:
            record.validity=record.date_deadline-record.create_date.date



    def accept_offer(self):
        estateProperty.accept_offer(price,partner_id)


    def reject_offer(self):
        pass


    # maxOffer=fields.Float(default='0', compute="_compute_max")

    # @api.depends("price")
    # def _compute_area(self):
    #     for record in self:
    #         if(maxOffer<price):
    #             maxOffer=price

    # @staticmethod
    # def getMaxOffer(self):
    #     return maxOffer


    
