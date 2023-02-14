from odoo import fields,models, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="list of property offers"

    price = fields.Float()
    status = fields.Selection(
        string = "Status",
        selection = [('accepted','Accepted'),('refused','Refused')],
        help  = "Status of offers",
        copy = False
        )
    
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)

    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(string="Deadline Date",compute="_compute_deadline", inverse="_inverse_deadline")

    @api.depends('validity')
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date.date() + relativedelta(days=+record.validity)

    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days
            