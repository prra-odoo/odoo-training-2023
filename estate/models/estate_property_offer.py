from datetime import date
from isodate import strftime
from odoo import models,fields,api,_
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Real Estate Property Offers"

    price=fields.Float()
    _order = "price desc"
    state=fields.Selection(
        copy=False,
        selection=[('accepted','Accepted'),('refused','Refused')]
    )
    
    partner_id=fields.Many2one("res.partner",string="Partner", required=True)
    property_id=fields.Many2one("estate.property",string="Property Id", required=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    #compute for date_deadline
    
    @api.depends("create_date","validity")
    
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else :
                record.date_deadline =  fields.Date.today() + relativedelta(days=record.validity)
                
    #inverse of date_deadline
         
    def _inverse_date_deadline(self):
        for record in self:
            print(record.validity)
            breakpoint()
            record.validity = int(record.date_deadline.strftime("%d")) - int(record.create_date.strftime("%d"))
            
        # strftime() used to convert datetime object into string
        # strftime("%d") to extract date
        # strftime("%m") for month 
        # strftime("%Y") for year
    
    # accept button method
    
    def action_accept(self):
        for record in self.property_id.offer_ids:
            record.state = "refused"
            self.state = "accepted"
            record.property_id.selling_price = self.price
            record.property_id.buyer_id = self.partner_id
            record.property_id.state = "accepted"
        return True
    
    # refuse button method
    
    def action_refuse(self):
        for record in self:
            record.state = "refused"
            record.property_id.selling_price = 0
            record.property_id.buyer_id = ""
            
        return True
    
    # SQL constraints
    
    _sql_constraints = [
        ("positive_price","check(price >= 0)","The offer price must be strictly positive")
    ]