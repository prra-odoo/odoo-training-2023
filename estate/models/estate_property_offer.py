from datetime import date
from isodate import strftime
from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offers"

    price = fields.Float()
    _order = "price desc"
    state = fields.Selection(
        copy=False, selection=[("accepted", "Accepted"), ("refused", "Refused")]
    )

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one(
        "estate.property", string="Property Id", required=True
    )
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(
        compute="_compute_date_deadline", inverse="_inverse_date_deadline"
    )
    property_type_id = fields.Many2one(
        related="property_id.property_type_id", store=True
    )
    # compute for date_deadline

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(
                    days=record.validity
                )
            else:
                record.date_deadline = fields.Date.today() + relativedelta(
                    days=record.validity
                )

    # inverse of date_deadline

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline <= record.create_date.date():
                record.validity = 0
            else:
                diff = record.date_deadline - record.create_date.date()
                record.validity = diff.days

        # record.validity = int(record.date_deadline.strftime("%d")) - int(record.create_date.strftime("%d"))
        # strftime() used to convert datetime object into string
        # strftime("%d") to extract date
        # strftime("%m") for month
        # strftime("%Y") for year

    # accept button method

    def action_accept(self):
        for record in self.property_id.offer_ids:
            record.state = "refused"
            self.state = "accepted"
            record.property_id.selling_price = self.price
            record.property_id.buyer_id = self.partner_id
            record.property_id.state = "accepted"
        return True

    # refuse button method

    def action_refuse(self):
        for record in self:
            record.state = "refused"
            record.property_id.selling_price = 0
            record.property_id.buyer_id = ""

        return True

    # SQL constraints

    _sql_constraints = [
        (
            "positive_price",
            "check(price >= 0)",
            "The offer price must be strictly positive",
        )
    ]

    @api.model
    def create(self, vals_list):

        estate_property_object = self.env["estate.property"].browse(
            vals_list["property_id"]
        )

        if vals_list["price"] <= estate_property_object.best_offer:
            raise UserError(_("Price must be greater than existing offer"))

        estate_property_object.state = "received"

        return super().create(vals_list)

    # vals_list
    # {'price': 456345678876678, 'validity': 7, 'date_deadline': '2023-03-08', 'partner_id': 14, 'state': False, 'property_id': 12}

    # we have not saved the record yet hence there is no record in self but the record is in
    # vals_list
    # self.env['estate.property'].browse(20)
    # this will give the record in estate.property model for id = 20
    # here we dont know id so we are using vals_list which contains the dic with all field name as key and value
    # vals_list is a dict and estat_property_obj is a object
