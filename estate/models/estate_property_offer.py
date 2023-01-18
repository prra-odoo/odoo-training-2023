# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta


class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"

    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    # start_date=fields.Date(string="start",default=date.today())
    # end_date=fields.Date(string="end",default=date.today()+relativedelta(days=+1))
    # days=fields.Integer(string="days",compute="_compute_days")
    
    # validity = fields.Integer(string="Validity")
    # date_deadline = fields.Date(
    #     compute="_compute_deadline", inverse="_inverse_deadline", string="Deadline")
    # create_date = fields.Date(default=date.today())

    # @api.depends("validity")
    # def _compute_deadline(self):
    #     for record in self:
    #         record.date_deadline = record.create_date + \
    #             relativedelta(days=+record.validity)

    # def _inverse_deadline(self):
    #     for record in self:
    #         x = date(record.date_deadline) - date(record.create_date)
    #         record.validity = x.days
    # @api.depends("end_date")
    # def _compute_days(self):
    #     # for record in self:
    #     #     record.date_deadline = record.create_date + \
    #     #         relativedelta(days=+record.validity)
    #     # self.end_date-self.start_date
    #     x=self.end_date - self.start_date
    #     print("this is the x------------------------------------------------------")
    #     self.days=x.days
    #     print(x.days)
    #     print(type(x.days))
    #     print(type(self.end_date))

