from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real-estate property offer"


    price= fields.Float()
    status=fields.Selection(
        string="Status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False
    )
    partner_id=fields.Many2one('res.partner',string='Partner')
    property_id=fields.Many2one('estate.property')
    validity=fields.Integer(default="7",string="Validity(days)")
    date_deadline=fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline",string="Deadline")

    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.date_deadline:
             record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity=(record.date_deadline - record.create_date.date()).days

            