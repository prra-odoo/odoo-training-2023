from odoo import models,fields,api
from odoo.tools.date_utils import add
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare




class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate Property Offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection( selection = [("accepted","Accepted"),("refused","Refused")],copy = False)
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('estate.property' , required=True)
    validity = fields.Integer(default= 7)
    date_deadline = fields.Date(compute = "_deadline", inverse ="_validity_change")
    create_date = fields.Date(default=fields.Datetime.now())
    property_type_id = fields.Many2one('estate.property.type',related="property_id.property_type_id" , store=True,string="property Type id")

    _sql_constraints=[
         (
            'check_offer_price' , 'CHECK(price>=0)',
            'Offers must be positive ')
    ]

    @api.depends("validity","date_deadline","create_date")
    def _deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days = record.validity)
            

    def _validity_change(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days 
    

    def accepted_offer(self):
       
        for record in self.search([('status', '=', 'accepted')]):
            # print(record)
            if record.property_id == self.property_id:
                for rec in record.search([('status', '=', 'accepted')]):
                    print(rec.property_id)
                    if rec.partner_id != record.partner_id:
                        raise UserError("one offer already accepted")
                    else:
                        rec.status = "refused"
        self.status = "accepted"
        self.property_id.buyer_id = self.partner_id
        self.property_id.selling_price = self.price
        self.property_id.state = "offer_accepted"
      

    def rejected_offer(self):
        for record in self:
            record.status = "refused"

#   inheritance
    # @api.model
    # def create(self, vals):
    #     self.env['estate.property'].browse(vals['property_id']).state='offer_recieved'
    #     breakpoint()
    #     return super().create(vals)
    @api.model
    def create(self, vals):
        if self.price:
            max_price = max(record.mapped('self.price'))
            if float_compare(vals['price'], max_price ,precision_rounding=0.01) <=0:
                raise UserError("the offer price must be higher than %.2f" % max_price)
        record = self.env['estate.property'].browse(vals['property_id'])
        record.state = 'offer_recieved'
        return super().create(vals)
        
        

