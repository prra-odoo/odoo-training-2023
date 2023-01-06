# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, time
from odoo.tools.float_utils import float_compare

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate advertisement module"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "sequence desc, property_type_id desc"

    name = fields.Char('Name',required=True)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer',tracking=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type') #inverse in property type
    description = fields.Text('Details',copy=False)
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From',default=lambda self:fields.Datetime.now(),readonly=True)
    expected_price = fields.Float('Expected price')
    selling_price = fields.Float('Selling price')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    bedrooms = fields.Integer('Bedroom',default='2')
    living_area = fields.Integer('Living area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden area(sqm)')
    tag_ids = fields.Many2many("estate.property.tag", string="Tags") # orm object
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),('offer_accepted', 'Offer Accepted'),('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',tracking=True
    )
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    total_area = fields.Float('Total Area(sqm)',compute='_compute_area')
    best_price = fields.Float('Best Price',compute='_compute_best_price')

    # method to calculate total area
    @api.depends('living_area', 'garden_area')
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(self.offer_ids.mapped('price'),default=0)

    def property_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError(('Cancelled property can not be sold.'))
            else:    
                record.state = 'sold'
        return True
        
    def property_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError(('Sold property can not be cancelled.'))
            else:
                record.state = 'canceled'
        return True

    # constraint
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 'The expected price must be stricly positive.'),
        ('check_selling_price', 'CHECK(selling_price > 0)', 'The selling price must be stricly positive.'),
    ]
    # python constraint
    @api.constrains('selling_price','expected_price')
    def _check_selling(self):
        for record in self:
            if float_compare(record.selling_price,0.9*record.expected_price,precision_digits =2) == -1:
                raise ValidationError('The selling price must be 90% of the expected price')
            