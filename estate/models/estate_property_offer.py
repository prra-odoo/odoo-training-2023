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
        string="Date Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("validity")
    def _compute_date_deadline(self):
        print("INSIDE COMPUTE-----------------------------------------------------------------------")
        for record in self:
            if (record.create_date):
                record.date_deadline = fields.Date.add(
                    record.create_date, days=record.validity)
            else:
                record.date_deadline = False

    def _inverse_date_deadline(self):
        print("------------------INVERSE------------------------------------------------------------")
        for record in self:
            if (record.date_deadline <= record.create_date.date()):
                record.validity = 0
            else:
                diff_days = record.date_deadline-record.create_date.date()
                record.validity = diff_days.days
