from odoo import models,fields,api,_
from dateutil.relativedelta import relativedelta

class EstateOffers(models.Model):
    _name= 'estate.property.offer'
    _description = 'Offer to estate property'

    price = fields.Float()
    status = fields.Selection(
        string= "Status",
        selection= [('accepted','Accepted'),('refused','Refused')],
        copy= False)
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=7)
    date_deadline= fields.Date(compute="_compute_date_deadline",inverse="_inverse_date")

    @api.depends("validity","create_date")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today()+ relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            record.validity= (record.date_deadline - record.create_date.date()).days

    


    def accept_action_estate_offer(self):
        self.status="accepted"
        self.property_id.selling_price= self.price
        self.property_id.buyer_id=self.partner_id

    def refuse_action_estate_offer(self):
        self.status="refused"
        self.property_id.selling_price= 0.0

    _sql_constraints=[(
        'offer_price_positive','CHECK(price>0)',
        'Offere  Price Must be positive'
    )]