import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is an Estate Property offers Model"

    price = fields.Float(string="Price", required=True)
    status = fields.Selection(copy=False, selection=[
                              ("act", "Accepted!"), ("ref", "Refused!")])

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner", required=True)

    property_id = fields.Many2one(
        comodel_name="estate.property", string="Property", required=True)

    validity = fields.Integer(string="Validity (Days)", default=7)

    date_deadline = fields.Date(
        string="Date Deadline", compute='_compute_date_deadline')

    @api.depends("date_deadline", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if (record.create_date <= datetime.datetime.today()):
                record.date_deadline = record.create_date + \
                    fields.Date.add(relativedelta(days=record.validity))
            else:
                pass

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = record.date_deadline-fields.Date.today()
