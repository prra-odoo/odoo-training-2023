# -*- coding: utf-8 -*-


from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare


class realEstate(models.Model):
    _name = "estate.property"
    _description = "This is the Database for the all clients and their requirements"
    _order = "id desc"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char("Name", required=True)
    # biography = fields.Html()
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date(
        "Available From", default=fields.Datetime.now()+relativedelta(months=3))
    expected_price = fields.Float("Excepted Price",default="120.00")
    selling_price = fields.Float("Selling Price", readonly=True, tracking=True)
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
        "res.users", string="Salesperson")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    company_id = fields.Many2one('res.company', string="Company")
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
            ('canceled', 'Canceled')], default="new", tracking=True
    )
    image = fields.Binary('image')
    color= fields.Integer()


    _sql_constraints = [
        ("check_excepted_price", "CHECK(selling_price > 0)",
         "Selling Price Must Be Positive"),
        ("check_excepted_price", "CHECK(expected_price > 0)",
         "Expected Price Must Be Positive"),
    ]

    @api.constrains("expected_price", "selling_price")
    def _check_selleing_price(self):
        for rec in self:
            if rec.selling_price != 0:
                if float_compare(rec.selling_price, (rec.expected_price * 0.9), precision_digits=3) < 0:
                    raise ValidationError(
                        "selling price cannot be lower than 90% of the expected price")
            else:
                pass

    # Compute Functions
    @api.depends("living_area", "garden_area")
    def _total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    @api.depends("garden")
    def _garden_area_total(self):
        for rec in self:
            if rec.garden:
                rec.garden_area = 1
            else:
                rec.garden_area = 0

    def _inverse_garden_area(self):
        for rec in self:
            if rec.garden_area > 0:
                rec.garden = True
            else:
                rec.garden = False

    @api.depends("offer_ids.price")
    def _best_price(self):
        for rec in self:
            rec.best_price = max(rec.offer_ids.mapped('price'), default=0)

    # Buttons

    def action_cancel_button_header(self):
        for rec in self:
            if rec.state == "sold":
                raise UserError("Sold Property can't be calceld")
            else:
                rec.state = "canceled"
            return True

    def action_sold_button_header(self):
        for rec in self:
            if rec.state == "canceled":
                raise UserError("Canceld property can't be sold")
            else:
                rec.state = "sold"
            return True

    @api.ondelete(at_uninstall=False)
    def _delete_property(self):
        for rec in self:
            if not (rec.state in ['new', 'canceled']):
                raise UserError("Can't Remove The Property.")

    @api.model
    def create(self,vals):
        print('estate property create method:',vals)
        return super(realEstate,self).create(vals)

    def write(self,vals):
        print('estate property write method:',vals)
        return super(realEstate,self).write(vals)
    