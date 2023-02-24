from odoo import fields,models, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="list of property offers"
    _order = "price desc"

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
    property_type_id = fields.Many2one('estate.property.type',related = "property_id.property_type_id",
                                        string="Property Type", store=True)
    #extra field for kanban view
    color = fields.Integer(string="Color", compute="_compute_color")


    # store attribute is use to control storage of data in DB with computaation and without change
    date_deadline = fields.Date(string="Deadline Date",compute="_compute_dead", inverse="_inverse_deadline", store=True)
    

    # set sql validation
    # if in table already have rows and that row not follow constraints then 
    _sql_constraints = [
        (
            'check_offer_prices_possitive',
            'CHECK(price > 0.0)',
            "Offer price are not be negative."
        )
    ]

        
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
            record.property_id.state = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id=record.partner_id
        

    #refuse button action
    def action_do_refuse(self):
        for record in self:
            record.status = 'refused'
            record.property_id.state = 'received'

    @api.depends('status')
    def _compute_color(self):
        for record in self:
            if (record.status == 'accepted'):
                record.color = 3
            elif(record.status == 'refused'):
                record.color = 9
            else:
                record.color=0
    
   
        

            