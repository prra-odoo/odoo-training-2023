from odoo import models,fields,api,exceptions
from dateutil.relativedelta import relativedelta
from datetime import datetime

class EstatePropertyOffer(models.Model):
    
    _name = "estate.property.offer"
    _description = "Property Offer Model"
    _order = "price desc"
    _sql_constraints = [
        ('validity', 'CHECK(validity >= 0)',
'The validity should be a positive number only.')
    ]
    _rec_name = "price"
    _inherits = {"estate.property":"property_id"}

    price = fields.Float()
    status = fields.Selection(
        string="Property status",
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False)
    partner_id = fields.Many2one("res.partner",string="partner",required=True)
    validity = fields.Integer(default = "7")
    property_id = fields.Many2one("estate.property",required=True)
    property_type_id = fields.Many2one("estate.property.type",string="Property Type",related='property_id.property_type_id', store=True)
    # create_date = fields.Date(default=fields.Datetime.today())

# for setting the deadline and even dynamically changing it
    date_deadline = fields.Date(compute="_compute_date",inverse="_inverse_date",store=True)
    @api.depends('create_date','validity')
    def _compute_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days = record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days = record.validity)            
            
    def _inverse_date(self):
        for record in self:
            if(record.date_deadline > datetime.date(datetime.today())):
                record.validity  = (record.date_deadline - record.create_date.date()).days
            else:
                raise exceptions.UserError("Set a date after today's")

            
            
# now from here the ACCEPT and REFUSE state code starts

    def accept_offer(self):
        for offers in self.property_id.offer_ids:
            offers.status = "refused"
        self.status="accepted"
        self.property_id.state="offer accepted"
        self.property_id.selling_price=self.price
        self.property_id.buyer_id=self.partner_id
        return True           
    def refuse_offer(self):
        self.status = "refused"
    
# now to check that the property selling price is not negative
    @api.constrains('price')
    def _check_offer_price(self):
        for property in self:
            if property.price <= 0:
                raise exceptions.ValidationError("offer price must be positive.")
            
    # color = fields.Integer(compute="_compute_color")
    # @api.depends('status')
    # def _compute_color(self):
    #     for record in self:
    #         if(record.status == 'accepted'):
    #             record.color = 10
    #         else:
    #             record.color = 2
