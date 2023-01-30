from odoo import api, fields, models
from datetime import timedelta
from odoo.exceptions import UserError
import datetime
 

class RealEstatePropertyOffer(models.Model):
    _name = "real.estate.property.offer"
    _description = "Property Offers"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused'),], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("real.estate.property", string="Property Name", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline_date", inverse="_inverse_deadline_date", store=True)
    property_type_id = fields.Many2one('real.estate.property.type',related='property_id.property_type_id',store=True)

    _sql_constraints = [('check_offer_price', 'CHECK(price > 0)', 'The price of an proerty should be greater than 0')]
    
    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        # print(fields_list)
        return res
    
    @api.depends('create_date', 'validity')
    def _compute_deadline_date(self):
        for record in self:
            for record in self:
                if record.create_date:  
                    record.date_deadline=record.create_date + timedelta(days=record.validity)
                else:
                    record.date_deadline = datetime.date.today() + timedelta(days=record.validity)
        
    def _inverse_deadline_date(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days

    def action_confirm(self):
        for record in self:
            record.status = 'accepted'
            record.property_id.state = 'offer_accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

    def action_cancel(self):
        for record in self:
            record.status = 'refused'
            
            
    @api.model
    def create(self, vals_list):
        for i in vals_list:
            rec = self.env['real.estate.property'].browse(vals_list['property_id'])
            rec.state =  'offer_received'
            if rec.best_price >= vals_list['price'] :
                raise UserError("you can not create an offer of lower amount than existing")
        return super().create(vals_list)