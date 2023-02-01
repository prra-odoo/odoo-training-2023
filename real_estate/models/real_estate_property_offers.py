from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class EstatePropertyOffers(models.Model):
    _name = "estate.property.offer"
    _description = "This model will contain estate property all the offers, price, status etc."

    # setting order of the list of offers in descending
    _order = "price desc"


    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)

    partner_id = fields.Many2one("res.partner")
    property_id = fields.Many2one("estate.property", required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date", inverse="_inverse_date")

    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)


    # defining sql constraints for the offer price
    _sql_constraints = [
        (
            'check_offer_price',
            'CHECK(price > 0)',
            'The offer price should be greater than 0'
        )
    ]


    @api.depends('validity')
    def _compute_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            record.validity = (record.date_deadline - date.today()).days


    
    @api.depends('status', 'price', 'property_id', 'partner_id')
    def action_confirm(self):
        
        for record in self:
            # id = record.property_id
            # record.status = 'accepted'
            # print(f"property_id.offer_ids{record.property_id.offer_ids}")
            # print(type(record.property_id.offer_ids))
            record.property_id.offer_ids.status = 'refused'
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = 'accepted'

    def action_reject(self):
        for record in self:
            record.status = 'refused'


    # python constraints to check whether the price is 90% of expected price
    @api.constrains('price', 'property_id')
    def price_percentage(self):
        for record in self:
            if float_compare(record.price, 0.90 * record.property_id.expected_price, precision_rounding=0.01) < 0:
                raise ValidationError(r"The offer price must be alteast 90% of expected price") 



    # Adding Create method which is an method exists in parent model
    @api.model
    def create(self, vals):
        record = self.env['estate.property'].browse(vals['property_id'])
        record.state = 'recieved'
        list_of_price = []
        for offer in record.offer_ids:
            list_of_price.append(offer.price)
        
        if len(list_of_price) != 0:
            if vals['price'] < max(list_of_price):
                raise UserError("The offer price must be more than the other offers!")

            
        return super(EstatePropertyOffers, self).create(vals)

    
    # def check_offers(self):
    #     property_id.offer_ids