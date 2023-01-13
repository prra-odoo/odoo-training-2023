# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This model will store the price related to estate"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Address of the building")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(copy=False, default=fields.datetime.today() + relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = "Type",
        selection = [("north", "North"), ("south", "South"), ("west", "West"), ("east", "East")]
    )
    active = fields.Boolean(default=True, string="Active")
    state = fields.Selection([("new","New"),("recieved","Offer Recieved"),("accepted","Accepted"),("sold","Sold"),("cancel","Canceled")], string="Status", copy=False, default="new")
    property_type_id = fields.Many2one("estate.property.type")
    buyer_id = fields.Many2one("res.partner", copy=False)
    seller_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", 'property_id')


    # sql constraints while setting expected price
    _sql_constraints = [
        (
            'check_expected_price',
            'CHECK(expected_price > 0)',
            'The expected price should be greater than 0'
        ),
        (
            'check_selling_price',
            'CHECK(selling_price > 0)',
            'The selling price should be greater than 0'
        )
    ]

    # computed fields
    # Note: By Default values of compute fields are read only 
    total_area = fields.Integer(compute="_compute_area")
    best_offer = fields.Float(compute="_compute_best_offer")


    @api.depends("living_area")
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    
    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price'), default=0)


    # Creating onchange functionality
    @api.onchange("garden")
    def _onchange_garden_toggle(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_orientation = ''
            self.garden_area = 0


    
    # Creating two button methods
    @api.depends('state')
    def sold_click(self):
        print(f"length of self : {len(self)}")
        for record in self:
            if record.state == "cancel":
                raise UserError("Once the property is Canceled it cannot be Sold!")
            else:
                record.state = "sold"


    def cancel_click(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Once the property is Sold it cannot be Canceled!")
            else:
                record.state = "cancel"


    def refresh_button(self):
        sum = 0
        for record in self:
            sum +=1 
            print(f"Type of self record : {type(record)}")
        print(f'Number of records {sum}')   