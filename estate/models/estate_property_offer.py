from odoo import models,fields,api,exceptions
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.tools import float_utils

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property offer model'
    _order = 'price desc'

    price = fields.Float()
    status = fields.Selection([('accepted','Accepted'),('refused','Refused')],copy=False)
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=0)
    date_deadline = fields.Date(compute = "_compute_date_deadline",inverse = "_inverse_date_deadline")

    _sql_constraints = [
        ("check_price","CHECK(price > 0)","The offer price must be strictly positive")
    ]

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
    def action_accept(self):
        for record in self.property_id.offer_ids:
            record.status = "refused"
        self.status = "accepted"
        self.property_id.selling_price = self.price
        self.property_id.state = "offer accepted"
        self.property_id.is_partner = True
    def action_refuse(self):
        self.status = "refused"
        self.property_id.selling_price = 0
    
    @api.constrains("date_deadline")

    def check_date_deadline(self):
        if(self.date_deadline  < fields.Date().today()):
            raise exceptions.ValidationError("The deadline can not be sent in the past.")
    
    