from odoo import api,models,fields
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateOfferProperty(models.Model):
    _name="real.estate.property.offer"
    _description="Property Offer Model"

    # name=fields.Char(string="name",required=True)
    price=fields.Float(string="Price")
    status=fields.Selection(string="status", selection=[('accepted','Accepted'),('refused','Refused')],copy=False)
    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('real.estate.properties',required=True)
    validity=fields.Integer(string="Validity", default=7)
    date_deadline=fields.Datetime(compute='_compute_date_deadline',inverse= "_inverse_date_deadline")

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline=record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline=fields.Datetime.now()+ relativedelta(days=record.validity)
    def _inverse_date_deadline(self):
        for record in self:
            record.validity=(record.date_deadline-record.create_date).days

    def action_accepted(self):
        for record in self:
            record.status='accepted'
            
    def action_refused(self):
        self.status='refused'

    