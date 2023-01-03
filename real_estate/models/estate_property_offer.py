
from odoo import fields, models, api
from odoo.tools.date_utils import add


class estatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

    price = fields.Float('Price')
    status = fields.Selection(strig="Status", selection=[('accepted','Accepted'), ('refused','Refused')], copy = False)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property" , required=True)
    validity = fields.Integer('Validity', default=7)
    date_deadline = fields.Date('Date Deadline', compute="_compute_deadline", inverse = '_inverse_deadline')
    create_date = fields.Date(default=fields.Datetime.now(),string="Create Date",readonly=True)

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = add(record.create_date, days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date).days

    
    def action_accept(self):
        for record in self:
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
        return True
    
    def action_refused(self):
        for record in self:
            record.status = "refused"
        return True