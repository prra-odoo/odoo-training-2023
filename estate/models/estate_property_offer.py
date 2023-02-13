from odoo import api,fields, models
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy = False
    )
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")
    @api.depends('create_date','validity')
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + timedelta(days = record.validity)

    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days


    