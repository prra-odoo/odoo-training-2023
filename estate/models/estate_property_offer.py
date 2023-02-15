from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "It's a Estate Property Offer"

    price = fields.Float()
    status  = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')
    ],
    copy=False,
    )
    partner_id = fields.Many2one("res.partner",string="buyer",required=True)
    property_id = fields.Many2one("estate.property",string="Property ID",required=True)
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute = "_compute_date_deadline",inverse="_inverse_date_deadline")

    # # Computed Fields
    @api.depends("validity","create_date")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity) 
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days
