from odoo import fields,models,api
from datetime import timedelta,datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

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
    
    _sql_constraints=[
        ('check_price','CHECK(price > 0)','Offer price must be positive')
    ]
   

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
        

    def action_accept(self):
        for record in self:
             for rec in self.property_id.offer_ids:
                if(rec.status == "accepted") >0:
                      raise UserError("You cannot select")
                
                
        record.status="accepted"
        record.property_id.selling_price=self.price
        record.property_id.buyer_id=self.partner_id

                
    def action_refuse(self):
        for record in self:
            record.status="refused"


