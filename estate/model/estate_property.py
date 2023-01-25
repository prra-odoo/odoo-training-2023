# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, time
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate advertisement module"
    _inherit = ['mail.thread','mail.activity.mixin'] #to add the chatter 
    _order = "sequence, property_type_id desc"

    name = fields.Char('Name',required=True)
    salesperson_id = fields.Many2one('res.users', string='Salesperson') #user_id
    buyer_id = fields.Many2one('res.partner', string='Buyer',tracking=True) #partner_id
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    description = fields.Text('Details',copy=False)
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From',default=lambda self:fields.Datetime.now(),readonly=True)
    expected_price = fields.Float('Expected price')
    selling_price = fields.Float('Selling price')
    sequence = fields.Integer('Sequence')
    bedrooms = fields.Integer('Bedroom',default='2')
    living_area = fields.Integer('Living area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden area(sqm)',compute='_compute_garden_area')
    total_area = fields.Float('Total Area(sqm)',compute='_compute_area')
    best_price = fields.Float('Best Price',compute='_compute_best_price')
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
    tag_ids = fields.Many2many("estate.property.tag", string="Tags") #relation table --> estate_property_estate_property_tag_rel
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    

    # method to calculate total area
    @api.depends('living_area', 'garden_area')
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('garden')
    def _compute_garden_area(self):
        if self.garden:
            self.garden_area=10
            self.garden_orientation= "north"
        else:
            self.garden_area=0
            self.garden_orientation=False

    # compute to get best price
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(self.offer_ids.mapped('price'),default=0)

    #sold action
    def property_sold(self):
        for record in self: #self --> recordset/collection --> gives record one by one
            if record.state == 'canceled':
                raise UserError('Canceled property can not be sold.')
            else:    
                record.state = 'sold'
        return True
        
    #cancel action   
    def property_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('Sold property can not be canceled.')
            else:
                record.state = 'canceled'
        return True

    #ondelete
    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_cancel(self):
        for record in self:
            if record.state not in ['new', 'canceled']:
                raise UserError("Only new and canceled property can be deleted.")
        #ondelete 
        # at_uninstall (bool) – Whether the decorated method should be called 
        # if the module is being uninstalled. 
        # If False, the module uninstallation does not trigger those errors.

    # constraint --> name, condition, message, list of tuples 
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 'The expected price must be stricly positive.'),
        ('check_selling_price', 'CHECK(selling_price > 0)', 'The selling price must be stricly positive.'),
    ]
    # python constraint
    # The decorator specifies which fields are involved in the constraint. 
    # The constraint is automatically evaluated when any of these fields are modified
    @api.constrains('selling_price','expected_price')
    def _check_selling(self):
        for record in self:
            if float_compare(record.selling_price,0.9*record.expected_price,precision_digits=2) <= 0:
                raise ValidationError('The selling price must be 90% of the expected price')


