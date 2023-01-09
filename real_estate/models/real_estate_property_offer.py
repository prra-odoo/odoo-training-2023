from odoo import fields,models,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
class RealEstatePropertyOffer(models.Model):
    _name="real.estate.property.offer"
    _description="Property Offer"
    price=fields.Float()
    status=fields.Selection(selection=[("accepted","Accepted"),("refused","Refused")],copy=False)
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("real.estate.property",required=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Datetime(compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    
    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline=record.create_date+relativedelta(days=record.validity)
            else:
                record.date_deadline=fields.Datetime.now()+relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            diff=record.date_deadline-record.create_date
            record.validity=int(diff.days)
