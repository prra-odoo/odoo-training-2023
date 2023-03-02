from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is an Estate Property offers Model"

    _sql_constraints = [("ofr_price_pos", "CHECK (price>=0)",
                         "The offer price must be greater than 0."),]
    _order = "price desc"

    price = fields.Float(string="Price", required=True)
    status = fields.Selection(copy=False, selection=[
                              ("act", "Accepted!"), ("ref", "Refused!")])

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner", required=True)

    property_id = fields.Many2one(
        comodel_name="estate.property", string="Property", required=True, ondelete="cascade", store=True)
    # Here ondelete="cascade" means that the property will be deleted even if it has offers, before it was
    # violating the foreign key constraint. Because a deleted property cannot have it's offers present in
    # the estate.property.offer table. The corresponding offers will also be deleted.

    validity = fields.Integer(string="Validity (Days)", default=7)

    date_deadline = fields.Date(
        string="Date Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    property_type_id = fields.Many2one(
        related="property_id.property_type_id", string="Property Type", store=True)

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
            # To set the offers, other than the accepted offer as refused.
            # First all offers are set REFUSED then the particular offer is set ACCEPTED.
            for var in self.property_id.offer_ids:
                var.status = "ref"
            self.property_id.state = "OA"
            self.status = "act"
            # breakpoint()
            self.property_id.selling_price = self.price
            self.property_id.buyer_id = self.partner_id

    def reject_offer(self):
        for record in self:
            record.status = "ref"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # breakpoint()
            # vals_list = [{'price': 123, 'partner_id': 27, 'validity': 7,
            # 'date_deadline': '2023-03-08', 'status': False, 'property_id': 6}]
            # The browse will fetch and give you the property under which we are adding offers,
            # using property_id. property_id is provided by vals.
            # vals is a dictionary and estate_property_obj is an object of the class estate.property,
            # and this is the reason (.best_price) works while (vals.property_id) doesen't.
            estate_property_obj = self.env['estate.property'].browse(
                vals['property_id'])
            if (vals['price'] < estate_property_obj.best_price):
                raise ValidationError(
                    "Cannot offer a price that is less than the current best price available.")
            estate_property_obj.state = "OR"
        return super().create(vals)

    @api.ondelete(at_uninstall=False)
    def mark_new_zero_offer(self):
        count = self.env['estate.property.offer'].search_count(
            domain=[('id', 'in', self.property_id.offer_ids.ids)])
        print(count, "--------------------------")
        if (count == 1):
            self.property_id.state = "N"
