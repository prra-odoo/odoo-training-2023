from odoo import models,fields,api
from odoo.tools.date_utils import add
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError




class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate Property Offer"

    price = fields.Float()
    status = fields.Selection( selection = [("accepted","Accepted"),("refused","Refused")],copy = False)
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('estate.property' , required=True)
    validity = fields.Integer(default= 7)
    date_deadline = fields.Date(compute = "_deadline", inverse ="_validity_change")
    create_date = fields.Date(default=fields.Datetime.now())


    _sql_constraints=[
         (
            'check_offer_price' , 'CHECK(price>=0)',
            'Offers must be positive ')
    ]

    @api.depends("validity","date_deadline","create_date")
    def _deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days = record.validity)
            

    # @api.depends("validity","date_deadline","create_date")
    def _validity_change(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days 
    

    def accepted_offer(self):
        for record in self.search([('status','=','accepted')]):
            raise ValidationError("Only one should be accepted at a time")
        self.status = "accepted"
        self.property_id.selling_price=self.price
        self.property_id.buyer_id = self.partner_id
            

    def rejected_offer(self):
        for record in self:
            record.status = "refused"

  









# x=0
#         for record in self:
            
#             if record.status == "accepted":
#                 x=x+1

#         if x==0:
#             for record in self:
#                  record.status = "accepted"
#                  record.property_id.selling_price=record.price
#                  record.property_id.buyer_id = record.partner_id
    
