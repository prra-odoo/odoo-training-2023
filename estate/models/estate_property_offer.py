from odoo import api,models,fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

class EstatePropertyOffer(models.Model):
    _name='estate.property.offer'
    _description='adding property tags in property'

    price=fields.Float(string='Price',
		help="this is for property offer price")
    status=fields.Selection(selection=[('accepted','Accepted'),('refused','Refused')],
		copy=False,
		string="status")
    partner_id=fields.Many2one('res.partner',
        string="Partner",
        required=True)
    property_id=fields.Many2one('estate.property',
        required=True,
        string="Property")
    validity=fields.Integer(string="Validity(days)",
      default=7)
    date_deadline=fields.Date(compute="_compute_deadline",string="Deadline",inverse="_inverse_deadline")
    @api.depends("validity","create_date")
    def _compute_deadline(self):
      for record in self:
        if record.create_date:
          record.date_deadline=record.create_date.date() + relativedelta(days=record.validity)
        else:
          record.date_deadline=fields.Date.today()+relativedelta(days=record.validity)
    def _inverse_deadline(self):
      for record in self:
        if(record.date_deadline>datetime.date(datetime.today())):
          record.validity=(record.date_deadline - record.create_date.date()).days

    def action_accept(self):
      for record in self:
        record.status="accepted"
        record.property_id.selling_price=record.property_id.best_price
        record.property_id.buyer_id=record.partner_id

    def action_refuse(self):
      for record in self:
        record.status="refused"
        