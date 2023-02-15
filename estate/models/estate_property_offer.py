from datetime import date
from isodate import strftime
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Real Estate Property Offers"

    price=fields.Float()
    status=fields.Selection(
        copy=False,
        selection=[('accepted','Accepted'),('refused','Refused')]
    )
    
    partner_id=fields.Many2one("res.partner",string="Partner", required=True)
    property_id=fields.Many2one("estate.property",string="Property Id", required=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_date_deadline",inverse = "_inverse_date_deadline")
    
    #compute for date_deadline
    
    @api.depends("create_date","validity")
    
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else :
                record.date_deadline = False 
                
    #inverse of date_deadline
         
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = int(record.date_deadline.strftime("%d")) - int(record.create_date.strftime("%d"))
            
        #strftime() used to convert datetime object into string
        #strftime("%d") to extract date
        #strftime("%m") for month 
        #strftime("%Y") for year