# -*- coding:utf:8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Advertisement module"
    _order = "id desc"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Name', required=True)
    postcode = fields.Char(string='Postcode')

    description = fields.Text(string='Description')

    image_customer = fields.Image(string="Image")

    date_availability = fields.Date(
        string='Date Available', default=lambda self: fields.Datetime.now())

    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    garden_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garden_area = fields.Integer(string='Garden Area')
    total_area = fields.Integer(compute="_compute_total_area")

    active = fields.Boolean(default=True)
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')

    selling_price = fields.Float(string='Selling Price', readonly=True)
    best_price = fields.Float(compute='_compute_best_price')
    expected_price = fields.Float(string='Price', required=True)

    state = fields.Selection(default="new", tracking=True,
                             selection=[('new', 'New'),
                                        ('offer_received', 'Offer Received'),
                                        ('offer_accepted', 'Offer Accepted'),
                                        ('sold', 'Sold'), ('maintenance',
                                                           'Maintenance'),
                                        ('cancel', 'Cancel')]
                             )
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[('south', 'South'), ('west', 'West'),
                                                     ('north', 'North'), ('east', 'East')]
                                          )

    # Relations fields
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    salesperson_id = fields.Many2one(
        'res.users', string="Sales Person", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    company_id = fields.Many2one('res.company', 'Company'
                                 )

    # company_id = fields.Many2one('res.company', store=True, copy=False,
    #                              string="Company",
    #                              default=lambda self: self.env.user.company_id.id)
    # currency_id = fields.Many2one('res.currency', string="Currency",
    #                               related='company_id.currency_id',
    #                               default=lambda
    #                               self: self.env.user.company_id.currency_id.id)
    currency_id = fields.Many2one('res.currency', string="Entry Fee")
    fee = fields.Monetary(string="Fee")

    # SQL Constraints
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)',
         'UserError : Enter the Validate Price'),
        ('check_selling_price', 'CHECK(selling_price >= 0)',
         'UserError : Enter the Validate Price')
    ]

    # Compute Method Call
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        """
        Compute perform sum and give to other fields
        """
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        """
        if you add multiple offer but in best_price field always get 
        max price in those offers using mapped and max function
        """
        for record in self:
            record.best_price = max(
                record.offer_ids.mapped('price'), default=0)

    def action_sold(self):
        """
        In action_sold (button), if user trigger that automatically state 
        to be change in sold and if state is cancle that offer must be 
        not sold.
        """
        for record in self:
            if record.state == 'cancel':
                raise UserError("cancel Properties cannot be sold")
            record.state = 'sold'
        return True

    def action_cancel(self):
        """
        In action_cancel (button),it is inverse of @action_sold 
        function
        """
        for record in self:
            if record.state == 'sold':
                raise UserError("sold Properties cannot be canceled")
            record.state = 'cancel'
        return True

    # Python Constrains
        """
        this constrains,elling price cannot be lower than 90% of 
        the expected price
        """
    @api.constrains("expected_price", "selling_price")
    def _check_selleing_price(self):
        if self.selling_price != 0:
            if float_compare(self.selling_price, (self.expected_price * 0.9), precision_digits=3) < 0:
                raise ValidationError(
                    "selling price cannot be lower than 90% of the expected price")
        else:
            pass

    # unlink(delete) method
        """
        when user in new or canceled of state,only that customer or
        form will be deleted other state must be not deleted.     
        """

    def unlink(self):
        for record in self:
            if record.state not in ['new', 'canceled']:
                raise UserError(
                    "Only New and Cancel Property will be Deleted.")
            return super().unlink()
