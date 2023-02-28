from odoo import models, fields, api, exceptions
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"
    _order = "id desc"
    _inherit = "inheritance.demo"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime(
        "Last seen", default=lambda self: fields.Datetime().now())
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        "Available from", default=lambda self: fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, default=0)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute="_compute_garden", readonly=False)
    garden_orientation = fields.Selection(selection=[("north", "North"), ("south", "South"), (
        "east", "East"), ("west", "West")], compute="_compute_garden", readonly=False)
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[("new", "New"), ("offer received", "Offer Received"), ("offer accepted", "Offer Accepted"), (
        "sold", "Sold"), ("canceled", "Canceled")], default="new", copy=False, readonly=True, store=True)
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    sales_person_id = fields.Many2one(
        'res.users', string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one(
        'res.partner', string="Buyer", compute="_compute_buyer_id")
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Float(compute="_compute_area")
    best_price = fields.Float(compute="_compute_bestprice", default=0)

    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)",
         "The expetcted price must be strictly positive"),
        ("check_selling_price", "CHECK(selling_price >= 0)",
         "The selling price must be strictly positive"),

    ]

    @api.depends("living_area", "garden_area")
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_bestprice(self):
        for record in self:
            price_list = self.env["estate.property.offer"].search([("property_id","=",record.id)]).mapped("price")
            record.best_price = price_list and max(price_list)

    @api.depends("garden")
    def _compute_garden(self):
        for record in self:
            if (record.garden is True):
                record.garden_area = 10
                record.garden_orientation = "north"
            else:
                record.garden_area = 0
                record.garden_orientation = ""

    def action_sold(self):
        for record in self:
            if (record.state == "canceled"):
                raise exceptions.UserError(
                    "Canceled properties can't be sold!")
            else:
                record.state = "sold"
                print("=====================",
                      record.sales_person_id.property_ids)

    def action_cancel(self):
        for record in self:
            record.state = "canceled"

    @api.depends("offer_ids.status")
    def _compute_buyer_id(self):
        for record in self:
            flag = 0
            for field in record.offer_ids:
                if (field.status == "accepted"):
                    record.buyer_id = field.partner_id
                    flag = 1
            if (flag == 0):
                record.buyer_id = ""

    @api.constrains("selling_price", "expected_price")
    def check_selling_price(self):
        for record in self:
            if (record.selling_price != 0 and record.selling_price < record.expected_price * 0.9):
                raise exceptions.ValidationError(
                    "The selling price must be at least 90% of the expected price. You must reduce the expected price if want to accept the offer.")

    @api.ondelete(at_uninstall=False)
    def _unlink_property(self):
        for record in self:
            if (record.state not in ["new", "canceled"]):
                raise exceptions.UserError(
                    "Only new and canceled properties can be deleted!")
