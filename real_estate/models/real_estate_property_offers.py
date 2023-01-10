from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date

class EstatePropertyOffers(models.Model):
    _name = "estate.property.offer"
    _description = "This model will contain estate property all the offers, price, status etc."

    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)

    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date", inverse="_inverse_date")

    @api.depends('validity')
    def _compute_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            record.validity = (record.date_deadline - date.today()).days