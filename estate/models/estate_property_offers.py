# -- coding: utf-8 --
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffers(models.Model):
    _name = "estate.property.offers"
    _description = "estate property offer Model"

    price = fields.Float(string='Price')
    status = fields.Selection(
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False
    )
    buyer_id=fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property')
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days = record.validity)
            else:
                record.validity = 0    

    def _inverse_date_deadline(self): 
        for record in self:
            if(record.date_deadline > record.create_date.date()):
                record.validity = (record.date_deadline - record.create_date.date()).days

    # @api.depends('validity')
    # def _compute_date_deadline(self):
    #     for record in self:
    #         if record.validity:
    #             record.date_deadline = datetime.today().date() + timedelta(days = record.validity)
    #         else:
    #             record.date_deadline = False    

    # def _inverse_date_deadline(self): 
    #     for record in self:
    #         if record.date_deadline:
    #             record.validity = (record.date_deadline - fields.Date.today()).days
    #         else:
    #             record.validity = 0

    def action_accept_offer(self):
        for record in self.property_id.offer_ids:
            record.status = "refused"
        self.status = "accepted"
        self.property_id.state = "offer_accepted"
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.buyer_id
        return True

    def action_refuse_offer(self):
        self.status == "refused"
        self.property_id.selling_price = 0
        self.property_id.buyer_id = None
        return True
            
    _sql_constraints = [
        ('check_price',
        'CHECK(price > 0)',
        'Offer Price Must be Positive')
    ]