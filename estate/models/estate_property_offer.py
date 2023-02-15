from odoo import fields,models, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="list of property offers"
    _table = "offer_table"

    price = fields.Float()
    status = fields.Selection(
        string = "Status",
        selection = [('accepted','Accepted'),('refused','Refused')],
        help  = "Status of offers",
        copy = False,
        )
    
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)

    validity = fields.Integer(string="Validity", default=7)
    # store attribute is use to control storage of data in DB with computaation and without change
    date_deadline = fields.Date(string="Deadline Date",compute="_compute_dead", inverse="_inverse_deadline", store=True)

    # compute attribute is use to change value base on changes of any other fields and change after removing focus
    @api.depends('validity')
    def _compute_dead(self):
        for record in self:
            if (not record.create_date):
                record.create_date = fields.date.today()
            record.date_deadline = record.create_date.date() + relativedelta(days=+record.validity)

    # inverse attribute is use to change value base on changes of any other fields and change after saving the record
    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days


    #accept button action
    def action_do_accept(self):
        self.property_id.offer_ids.status = 'refused'
        for record in self:
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer=record.partner_id
        

    #refuse button action
    def action_do_refuse(self):
        for record in self:
            record.status = 'refused'
        
            