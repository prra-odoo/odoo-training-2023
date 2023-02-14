from odoo import api,fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy = False
    )
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")
    @api.depends('create_date','validity')
    def _compute_deadline(self):
        for record in self:
            if(not record.create_date):
                record.create_date = fields.Datetime.today()
            record.date_deadline = record.create_date + relativedelta(days = record.validity)

    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - datetime.date(record.create_date)).days

    # def accept_offer(self):
    #     for offers in self.property_id.offer_ids:
    #         offers.status = "refused"
    #     self.status="accepted"
    #     self.property_id.state="offer accepted"
    #     self.property_id.selling_price=self.price
    #     self.property_id.buyer_id=self.partner_id
    #     return True

    # def refuse_offer(self):
    #     self.status = "refused"


    