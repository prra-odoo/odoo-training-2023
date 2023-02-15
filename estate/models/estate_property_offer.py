from odoo import fields,models,api
from datetime import timedelta,datetime
from dateutil.relativedelta import relativedelta
class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Estate Property Offer"


    price=fields.Float(string="Price")
    status=fields.Selection(
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False    
        )

    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('estate.property',required=True)

    validity=fields.Integer(string="Validity",default="7")
    date_deadline=fields.Date(string="Deadline",compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                date = record.create_date.date()  
                record.date_deadline = date + relativedelta(days=record.validity)
            else:
                date=datetime.today()
                record.date_deadline = date + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline >= datetime.date(datetime.today()):
                record.validity= (record.date_deadline - record.create_date.date()).days
        
