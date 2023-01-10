from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class RealEstatePropertyOffer(models.Model):
    _name = "real.estate.property.offer"
    _description = "Property Offers"

    price = fields.Float(required=True)
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused'),], copy=False)
    partner_id = fields.Many2one(
        "res.partner", string="Partner", required=True)
    property_id = fields.Many2one(
        "real.estate.property", string="Property Name", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline_date")

    @api.depends('create_date', 'validity')
    def _compute_deadline_date(self):
        for record in self:
            record.date_deadline = record.create_date + \
                relativedelta(days=record.validity)
