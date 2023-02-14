from odoo import fields,models,api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Properties Offers"

    price = fields.Float(required=True)
    status = fields.Selection(
        string='Status',
        selection = [('accepted','Accepted'),('refused','Refused')],
        copy=False
     )
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_deadline")
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)

    # @api.depends('validity')    
    # def _compute_date(self):
    #     for record in self:
    #         record.date_deadline = record.create_date.date() + relativedelta(days=+record.validity)

    # def _inverse_date(self):
    #     for record in self:
    #         record.validity=(record.date_deadline-record.create_date).days()
    @api.depends('validity')
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date.date()+relativedelta(days=+record.validity)
    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days


