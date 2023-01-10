from odoo import api,fields,models
from dateutil.relativedelta import relativedelta
from datetime import date

class Estate_property_offer(models.Model):
    _name= "estate.property.offer"
    _description= "Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'),('refused','Refused')], copy=False)
    partner_id= fields.Many2one("res.partner",required=True)
    property_id= fields.Many2one("estate.property.model",required=True)
    validity = fields.Integer(default="7")
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")


    @api.depends('validity','create_date')
    def _compute_deadline(self):

        for record in self:
            # print("-----------------", record.create_date)
            if record.create_date == True:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + relativedelta(days=record.validity)


    def _inverse_deadline(self):
        
        for record in self:  
            record.validity=abs(record.create_date.date() - record.date_deadline).days
            
            # record.validity = (record.date_deadline - record.create_date.date()).days
        
