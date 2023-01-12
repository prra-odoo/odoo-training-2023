# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class estate_property(models.Model):
    _name = 'estate.property'
    _description = "Real Estate Module"

    property_type_id = fields.Many2one('estate.property.type',string='property type')

    name = fields.Char('Property Name',required=True)
    description = fields.Char('Description')
    postcode = fields.Char('PostCode')
    date_availability = fields.Date('Date',copy=False)
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',readonly=True,copy=False)
    bedrooms = fields.Integer('Bedrooms',default='2')
    living_area = fields.Integer('living area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage',default=True)
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden_area')
    garden_orientation = fields.Selection(
            string='Garden_orientation',default="South",
            selection=[('North','North'),('South','South'),('East','East'),('West','West')],
            help="This type is saparate north ,south,east and wast")
    active = fields.Boolean('Active',default=True)

    status = fields.Selection(
            string='Status',copy=False,default='New',
            selection=[('New','New'),('offer received','offer received'),('offer Accepted','offer Accepted'),('cancelled','cancelled'),('Sold','Sold')])
    
    salesperson = fields.Many2one('res.users',string="Salesperson",default=lambda self:self.env.user)
    buyer = fields.Many2one('res.partner',string="Buyer",copy=False)

    property_tag_ids = fields.Many2many('estate.property.tags',string='property tags')
    offer_ids = fields.One2many('estate.property.offer','property_id',string='property offer')
    total_area = fields.Float(compute="_compute_total_area")
    best_offer = fields.Float(default=0,compute="_compute_best_offer")


    _sql_constraints = [('check_expected_price','CHECK(expected_price >= 0)','A property expected price must be strictly positive.')]
    _sql_constraints = [('check_selling_price','CHECK(selling_price >= 0)','A property selling price must be strictly positive.')]


    @api.onchange("garden")
    def _onchange_garden(self):
            if self.garden == True:
                    self.garden_area = 10
                    self.garden_orientation = 'North'

    
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
            for record in self:
                    record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
             for record in self:
                     if record.offer_ids:
                             record.best_offer = max(record.offer_ids.mapped('price'))
                     else:
                             record.best_offer = 0


    def action_canceled(self):
            if self.status == 'Sold':
                    raise UserError("sold property can not be cancelled")
            else:
                    self.status = 'cancelled'


    def action_sold(self):
            if self.status == 'cancelled':
                    raise UserError("cancelled property can not be sold")
            else:
                    self.status = 'Sold'
                    
                    
    
     