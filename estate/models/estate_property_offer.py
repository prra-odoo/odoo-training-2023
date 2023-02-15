from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property offer model'

    price = fields.Float()
    status = fields.Selection([('accepted','Accepted'),('refused','Refused')],copy=False)
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=0)
    date_deadline = fields.Date(compute = "_compute_date_deadline",inverse = "_inverse_date_deadline")

    @api.depends("validity")

    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date().today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date:
                delta = record.date_deadline - fields.Date().today()
                record.validity = delta.days
            else:
                delta = record.date_deadline - record.create_date
                record.validity = delta.days
    