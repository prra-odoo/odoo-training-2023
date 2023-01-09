
from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError


class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _order = "price desc"

    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)','The Offer Price must be Positive')
    ]

    price = fields.Float('Price')
    status = fields.Selection(strig="Status", selection=[('accepted','Accepted'), ('refused','Refused')], copy = False)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property" , required=True)
    validity = fields.Integer('Validity', default=7)
    property_type_id = fields.Many2one(
        "estate.property.type", related = "property_id.property_type_id" ,string="Property Type", store=True)
    date_deadline = fields.Date('Date Deadline', compute="_compute_deadline", inverse = '_inverse_deadline')
    create_date = fields.Date(default=fields.Datetime.now(),string="Create Date",readonly=True)

   
    @api.depends('validity')
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days =+ record.validity)

    def _inverse_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date).days

    
    def action_accept(self):
        for record in self:
            if "accepted" in self.mapped("property_id.offer_ids.status"):
                raise UserError('no')
            else:
                
                record.status = "accepted"
                record.property_id.selling_price = record.price
                record.property_id.buyer_id = record.partner_id
        return True
    
    def action_refused(self):
        for record in self:
            record.status = "refused"
        return True

    # @api.model
    # def create(self, vals):
    #     max_offer = 0
    #     if vals.get("property_id") and vals.get("price"):
    #         rec = self.env['estate.property'].browse(vals['property_id'])
    #         max_offer = max(rec.mapped("offer_ids.price"))
    #         if max_offer > vals['price'] :
    #             raise UserError('The offer must be higher than %.2f" % max_offer')
    #     rec.state = 'received'
    #     return super().create(vals)