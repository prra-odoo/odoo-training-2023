from odoo import api,fields, models
from datetime import date
import dateutil.parser
from dateutil.relativedelta import relativedelta
from odoo import *
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"
    _order = "price desc"

    price = fields.Float(string="Price")
    status = fields.Selection(copy=False,selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.Many2one("res.partner",required=True)
    property_id = fields.Many2one("estate.property",required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date",inverse="_inverse_date")
    property_type_id = fields.Many2one(related = "property_id.property_type_id", string="Property Type",store=True)
    @api.depends("validity","date_deadline")
    def _compute_date(self):
        for record in self:
            record.date_deadline = fields.Date.today()+relativedelta(days=record.validity)
           
    def _inverse_date(self):
        for record in self:
            record.validity = (record.date_deadline - fields.Date.today()).days

    def action_accepted(self):
        for record in self.property_id.offer_ids:
            record.status = "refused"
        self.status ="accepted"
        self.property_id.buyer=self.partner_id
        self.property_id.selling_price=self.price
        self.property_id.state = "offer accepted"
        return True
    
    def action_refused(self):
        for record in self:
           if(record.status =='accepted'):
                record.property_id.selling_price = 0
                record.property_id.buyer = ""
        self.status = 'refused' 
        return True
    
    _sql_constraints = [
        ('check_price',"CHECK(price >= 0)","Offer price must be positive"),
    ] 

    @api.model
    def create(self, vals):
        property_record = self.env['estate.property'].browse(vals['property_id'])
        if (vals['price'] < property_record.expected_price):
            raise UserError("Offer should not be less than %d"%property_record.expected_price)
        return super().create(vals)
