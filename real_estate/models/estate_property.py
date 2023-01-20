# -*- coding: utf-8 -*-
from odoo import api,fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    postcode = fields.Integer('Postcode' ,required= True)
    date_availability = fields.Date('Date', default=lambda self: fields.Datetime.now(), readonly=True)
    expected_price = fields.Float('Expected price')
    selling_price = fields.Float('Selling price' , default = 0, copy = False)
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden area', default = "2500")
    total_area = fields.Integer('Total Area', compute="_compute_total_area")
    best_price = fields.Integer('Best Price', compute="_compute_best_price", default=0)
    status = fields.Char('Status', readonly=True, default="New", tracking=True)
    garden_orientation = fields.Selection(string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')],
        help="Type is used to separate Leads and Opportunities")
    state = fields.Selection(string = "state", selection = [('new', 'New'), ('received', 'Offer Received'), ('accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancel', 'Cancel')], default= "new")
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesman_id = fields.Many2one("res.users", string="Salesman" ,default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyers")
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer","property_id")
    # active = fields.Boolean('Active', default=False)

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The expected Price must be Positive'),
        ('check_selling_price', 'CHECK(selling_price > 0)',
         'The Selling Price must be Positive'),
    ]

    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'), default=0)
            # if record.offer_ids.status == 'accepted':


    def action_sold(self):
        for record in self:
            if record.status == 'Canceled':
                raise UserError('Canceled Property cannot be sold.')
            else:
                record.status = "Sold"
                record.state = 'sold'
      
    
    def action_cancel(self):
        for record in self:
            if record.status == 'Sold':
                raise UserError('Sold Property cannot be canceled.')
            else:
                record.status = "Canceled"
                record.state = 'cancel'
        
    
    @api.constrains("expected_price", "selling_price")
    def _check_price_difference(self):
        for rec in self:
            if (
                not float_is_zero(rec.selling_price, precision_rounding=0.01)
                and float_compare(rec.selling_price, rec.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price! "
                    + "You must reduce the expected price if you want to accept this offer."
                )

    
    @api.ondelete(at_uninstall=False)
    def _check_state(self):
        for asset in self:
            if asset.state not in ['new', 'cancel']:
                raise UserError(
                    'You cannot delete a data in this state.',
                )
