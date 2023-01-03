# -*- coding: utf-8 -*-

from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.tools.date_utils import add


class estatepropertyoffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers Model"

    price = fields.Float(string="Property Price:")
    status = fields.Selection(selection=[('accepted','Accepted'),('refuse','Refused')])
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",string="Property",required=True)
    validity = fields.Integer(string="Validity in Months",default=7)
    date_deadline = fields.Date(compute="_compute_deadline_date",inverse="_inverse_deadline_date")
    create_date=fields.Date(default=lambda self:fields.Datetime.today())

    @api.depends("validity","date_deadline")
    def _compute_deadline_date(self):
        for record in self:
            record.date_deadline= add(fields.Datetime.today(),days=record.validity)

    def _inverse_deadline_date(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    def action_accept(self):
        for record in self:
            record.status='accepted'
    
    def action_refuse(self):
        for record in self:
            record.status='refuse'

    # def action_refuse(self):
    #     for record in self:
    #         record.status='refuse'

    # (datetime.strptime(self.date_start,'%Y-%m-%d') + relativedelta(months=self.duree_mois)).strftime('%Y-%m-%d')

