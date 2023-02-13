from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    
    _name = "estate.property.offer"
    _description = "Property Offer Model"

    price = fields.Float()
    status = fields.Selection(
        string="Property status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False)
    partner_id = fields.Many2one("res.partner",string="partner",required=True)
    property_id = fields.Many2one("estate.property",required=True)
    validity = fields.Integer(default = "7")
    create_date = fields.Date(default=fields.Datetime.today())

# for setting the deadline and even dynamically changing it
    date_deadline = fields.Date(compute="_compute_date",inverse="_inverse_date",store=True)
    @api.depends('create_date','validity')
    def _compute_date(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            if record.create_date:
                record.validity  = (record.date_deadline - record.create_date).days


            
# now from here the ACCEPT and REFUSE state code starts

    def accept_offer(self):
        self.status = "accepted"
        
        
    
    def refuse_offer(self):
        self.status = "refused"
    