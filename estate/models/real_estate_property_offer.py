from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class EstatePropertyOfferModel(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate.property.offer'
    
    price = fields.Float(string="Price")
    status = fields.Selection(string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="status is used to show offer status",copy=False
    )
    partner_id = fields.Many2one('res.partner',required=True, index=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days= record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days= record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days

    def action_accept(self):
        for record in self:
            record.status='accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id
    
    def action_refuse(self):
        for record in self:
            record.status='refused'