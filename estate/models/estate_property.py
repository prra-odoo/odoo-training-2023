# -*- coding: utf-8 -*-

from odoo import fields, models, api, _, exceptions
from datetime import date
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The Expected Price must be positive.'),
         ('check_selling_price', 'CHECK(selling_price > 0)',
         'The Selling Price must be positive.'),
         
    ]

    name = fields.Char(string="Name", required=True, help="this is name")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Pin Code", required=True)
    date_availability = fields.Date(string="Availablity Date", copy=False, default=(
        date.today() + relativedelta(months=+3)))
    expected_price = fields.Float(
        string="Expected Price", required=True, default="1")
    selling_price = fields.Float(
        string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedroom Number", default="2")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(
        string="Garden Area", compute="_compute_garden", readonly=False, store=True)
    garden_orientation = fields.Selection(compute="_compute_garden", readonly=False, store=True,
                                          string="Garden Orientation",
                                          selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        string="State",
        tracking=True,
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),
                   ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancel', 'Canceled')],
        default='new',compute="_comput_state",readonly=False,store=True)
    salesperson_id = fields.Many2one(
        'res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False,readonly=True)
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    tags_ids = fields.Many2many(
        "estate.property.tags", 'property_under_tag_rel', 'property_id', 'tag_id', string="Tags")
    offer_ids = fields.One2many(
        "estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(
        compute="_compute_total_area", string="Total Property Area")
    best_offer = fields.Float(
        compute="_compute_best_offer", string="Best Offer")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
        
    @api.depends("best_offer")
    def _comput_state(self):
        for rec in self:
            if rec.best_offer > 0:
                rec.state = "offer_received"

    @api.ondelete(at_uninstall=False)
    def _unlink_if_state(self):
        if self.state not in ['new','cancel']:
            raise exceptions.UserError("Can't delete an Offer if not in new or canceled stage!")


    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(
                record.offer_ids.mapped("price"), default=0)
            

    @api.depends("garden")
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_orientation = 'north'
                record.garden_area = "10"
            else:
                record.garden_orientation = ''
                record.garden_area = ""

    def sold_buisness_logic(self):
        if self.state == 'cancel':
            raise exceptions.UserError("Canceled Property Can Not be sold")
        else:
            self.state = 'sold'
            return True

    def cancel_buisness_logic(self):
        if self.state == 'sold':
            raise exceptions.UserError("Sold Property Can Not be Canceled")
        else:
            self.state = 'cancel'
            return True


    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < .9*record.expected_price:
                raise exceptions.ValidationError(r"The selling price cannot be lower than 90% of the expected price")
