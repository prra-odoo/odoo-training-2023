# -*- coding: utf-8 -*-
from odoo import models,fields,api

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
    garden = fields.Boolean('Garden',default=True)
    garden_area = fields.Integer('Garden_area')
    garden_orientation = fields.Selection(
            string='Garden_orientation',default="South",
            selection=[('North','North'),('South','South'),('East','East'),('West','West')],
            help="This type is saparate north ,south,east and wast")
    active = fields.Boolean('Active',default=True)

    status = fields.Selection(
            string='Status',copy=False,default='New',
            selection=[('New','New'),('offer received','offer received'),('offer Accepted','offer Accepted'),('offer cancelled','offer cancelled'),('Sold','Sold')])
    
    salesperson = fields.Many2one('res.users',string="Salesperson",default=lambda self:self.env.user)
    buyer = fields.Many2one('res.company',string="Buyer",copy=False)

    property_tag_ids = fields.Many2many('estate.property.tags',string='property tags')
    offer_ids = fields.One2many('estate.property.offer','property_id',string='property offer')
    total_area = fields.Float(compute="_compute_total_area")
    best_offer = fields.Float(default=0,compute="_compute_best_offer")


    @api.depends("garden")
    def _onchange_garden(self):
            if self.garden == True:
                    self.garden = 10
                    self.garden_orientation = 'North'


    
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
            for record in self:
                    record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
             for record in self:
                     record.best_offer = max(record.offer_ids.mapped('price'))

    
     