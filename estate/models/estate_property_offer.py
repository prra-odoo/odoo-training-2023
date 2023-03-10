from odoo import api,fields, models,exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _order = "price desc"
    _sql_constraints = [
        ('check_offer_price','CHECK(price>0)','The offer price must be strictly positive.'),
    ]

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy = False
    )
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)
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
            if(record.date_deadline > fields.Date.today()):
                record.validity = (record.date_deadline - datetime.date(record.create_date)).days
            else:
                raise exceptions.ValidationError("Deadline cannot be set in the past.")

    def action_accept_offer(self):
        for offers in self.property_id.offer_ids:
            offers.status = "refused"
        self.status="accepted"
        self.property_id.state="offer accepted"
        self.property_id.selling_price=self.price
        self.property_id.buyer_id=self.partner_id
        return True

    def action_refuse_offer(self):
        self.status = "refused"

    @api.model
    def create(self,vals):
        property = self.env['estate.property'].browse(vals['property_id'])
        if(vals['price'] < property.best_price):
            raise exceptions.UserError("Offer price cannot be less than best offer. i.e. %d" %property.best_price)
        property.state = 'offer received'
        return super().create(vals)

    
    
    