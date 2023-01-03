from odoo import models,fields,api
from odoo.tools.date_utils import add


class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate Property Offer"

    price = fields.Float()
    status = fields.Selection( selection = [("accepted","Accepted"),("refused","Refused")],copy = False)
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('estate.property' , required=True)
    validity = fields.Integer(default= 7)
    date_deadline = fields.Date(compute = "_deadline" , inverse ="_validity_change")
    create_date = fields.Date(default=fields.Datetime.now())

    @api.depends("validity","date_deadline","create_date")
    def _deadline(self):
        for record in self:
            record.date_deadline = add(record.create_date,days=record.validity)

    # @api.depends("validity","date_deadline","create_date")
    def _validity_change(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days 

    def accepted_offer(self):
        for record in self:
            record.status = "accepted"
            

    def rejected_offer(self):
        for record in self:
            record.status = "refused"   
    
