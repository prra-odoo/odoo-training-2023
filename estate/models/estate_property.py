# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.tools.date_utils import add
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare


class realEstate(models.Model):
    _name = "estate.property"
    _description = "This is the Database for the all clients and their requirements"
    _order = "id desc"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date(
        "Available From", default=add(fields.Datetime.now(), months=3))
    expected_price = fields.Float("Excepted Price")
    selling_price = fields.Float("Selling Price", readonly=True,tracking=True)
    bedrooms = fields.Integer("Bedrooms")
    living_area = fields.Integer("Living Area", default="1")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer(
        "Garden Area", compute="_garden_area_total", inverse="_inverse_garden_area")
    garden_orientation = fields.Selection(
        selection=[('small', 'Small'), ('big', 'Big')]
    )
    active = fields.Boolean(default=True)
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    salesperson_id = fields.Many2one(
        "res.users", string="Salesperson", default=lambda self: self.env.user, copy=False)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many(
        "estate.property.offer", 'property_id', string="Offer")
    total_area = fields.Integer(compute="_total_area", string="Total Area")
    best_price = fields.Float(compute="_best_price", string="Best Price")
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')], default="new", readonly=True,tracking=True
    )

    _sql_constraints = [
        ("check_excepted_price", "CHECK(selling_price > 0)",
         "Selling Price Must Be Positive"),
        ("check_excepted_price", "CHECK(expected_price > 0)",
         "Expected Price Must Be Positive"),
    ]

    @api.constrains("expected_price", "selling_price")
    def _check_selleing_price(self):
        if self.selling_price != 0:
            if float_compare(self.selling_price, (self.expected_price * 0.9), precision_digits=3) < 0:
                raise ValidationError(
                    "selling price cannot be lower than 90% of the expected price")
        else:
            pass

    # Compute Functions
    @api.depends("living_area", "garden_area")
    def _total_area(self):
        self.total_area = self.living_area + self.garden_area

    @api.depends("garden")
    def _garden_area_total(self):
        if self.garden:
            self.garden_area = 1
        else:
            self.garden_area = 0

    def _inverse_garden_area(self):
        if self.garden_area > 0:
            self.garden = True
        else:
            self.garden = False

    @api.depends("offer_ids.price")
    def _best_price(self):
        for rec in self:
            rec.best_price = max(rec.offer_ids.mapped('price'), default=0)

    # Buttons

    def action_cancel_button_header(self):
        if self.state == "sold":
            raise UserError("Sold Property can't be calceld")
        else:
            self.state = "canceled"
        return True

    def action_sold_button_header(self):
        if self.state == "canceled":
            raise UserError("Canceld property can't be sold")
        else:
            self.state = "sold"
        return True
