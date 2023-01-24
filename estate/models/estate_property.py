# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
import warnings

class Estate_Property(models.Model):
    _name = "estate.property"
    _description = "Property Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string = 'name',required=True)
    status = fields.Char(string='Status',default='new')
    property_type_id = fields.Many2one("estate.property.type", string = 'Property Type',)
    user_id = fields.Many2one('res.users', string='Salesperson',default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner',string = 'Buyer',copy=False)
    description = fields.Text(string = 'description')
    postcode = fields.Char(string = 'postcode', required = True)
    data_avabilability = fields.Date('Datetime',default=fields.Date.today()+relativedelta(months=3), copy=False)
    expected_price = fields.Float(string = 'expected price',required = True)
    selling_price = fields.Float(string = 'selling price')
    bedrooms = fields.Integer(string = 'bedrooms')
    living_area = fields.Integer(string = 'living area')
    facades = fields.Integer(string = 'facades')
    garage = fields.Boolean(string = 'garage')
    garden_area = fields.Integer(string = 'garden area')
    garden_orientation = fields.Selection(
        string = 'garden orientation',
        selection = [('north','North'),('south','South'),('east','East'),('west','West')]
    )
    state = fields.Selection(
        string = 'State',
        selection = [('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')]
    )
    tag_ids = fields.Many2many("estate.property.tag","estate_property_rel","property_id","property_tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer",'property_id',string="Offer")
    
    total_area = fields.Integer(string ='Total area', compute = "_compute_total_area")
    best_price = fields.Float(string ='Best Offer', compute = "_compute_best_price")


    #compute method
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    #best offer
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price"),default=0)         

    #buttons
    def action_sold(self):
        for record in self:
            record.status = "sold"
        return True  

    
    def action_cancle(self):
        for record in self:
            record.status = "cancle"
        return True          
