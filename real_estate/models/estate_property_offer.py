from odoo import fields,models,api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Properties Offers"
    _order="price desc"

    price = fields.Float(required=True)
    status = fields.Selection(
        string='Status',
        selection = [('accepted','Accepted'),('refused','Refused')],
        copy=False
     )
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_date",inverse="_inverse_date")
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)

    property_type_id = fields.Many2one(related = "property_id.property_type_id", store = True)


    #An offer price must be strictly positive
    _sql_constraints = [
        ('check_offerprice', 'CHECK(price >= 0)',
         'Offer Price Must Be In Possitive Value.')
    ]

    #Compute a validity date for offers.
    @api.depends('create_date','validity')
    # def _compute_date(self):
    #     for record in self:
    #         if(not record.create_date):
    #             record.create_date=fields.date.today()
    #         record.date_deadline = record.create_date.date()+relativedelta(days=+record.validity)

    #         @api.depends("create_date", "validity")
    def _compute_date(self):
        for record in self:
            if record.create_date:
                date = record.create_date.date()
                record.date_deadline = date + relativedelta(days=record.validity)
            else:
                date=datetime.today()
                record.date_deadline = date + relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            if(record.date_deadline > datetime.date(datetime.today())):
                record.validity = (record.date_deadline - record.create_date.date()).days
            else:
                record.validity=0

    #Accept and Refuse Action 
    # offer is accepted, set the buyer and the selling price for the corresponding property.
    def action_accept(self):
        for record in self:
            record.status="accepted"
            record.property_id.selling_price=record.price
            record.property_id.buyers_id=record.partner_id
            record.property_id.state = 'off_ac'

    def action_refused(self):
        for record in self:
            record.status="refused"

    