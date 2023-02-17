import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError


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
        for record in self:
            # Here we have used today's date, because when
            # creating a new record, create_date is unavailable.
            # print("CoMpUtE-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-")
            if (record.create_date):
                record.date_deadline = fields.Date.add(
                    record.create_date, days=record.validity)
            else:
                record.date_deadline = fields.Date.add(
                    fields.Date.today(), days=record.validity)

    def _inverse_date_deadline(self):
        # print("------------------------------------InVeRsE")
        for record in self:
            if (record.date_deadline <= record.create_date.date()):
                record.validity = 0
            else:
                diff_days = record.date_deadline-record.create_date.date()
                record.validity = diff_days.days

    def accept_offer(self):
        if (self.property_id.state == "OA"):
            raise UserError(
                ('More than one offer can not be accepted at the same time.'))
        else:
            for var in self.property_id.offer_ids:
                var.status = "ref"
            self.property_id.state = "OA"
            self.status = "act"
            self.property_id.selling_price = self.price
            self.property_id.buyer_id = self.partner_id

    def reject_offer(self):
        for record in self:
            record.status = "ref"
