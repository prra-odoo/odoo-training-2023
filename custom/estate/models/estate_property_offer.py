from odoo import api,models,fields
import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate property offer'

    price = fields.Float()
    status = fields.Selection(
        selection = [('accepted','Accepted'),('refused','Refused')],
        copy = False,
        required=False
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    validity = fields.Integer(default=7, string='Validity (days)')
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if (record.create_date):
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days

    def action_accept(self):
        for record in self.property_id.offer_ids:
            record.status = 'refused'   
            record.property_id.selling_price = self.price     
            record.property_id.buyer_id = self.partner_id
        self.status = 'accepted'
        return True     
    
    def action_refuse(self):
        for record in self:
            if(record.status == 'accepted'):
                record.property_id.selling_price = 0
                record.property_id.buyer_id = ''
            record.status = 'refused'
        return True