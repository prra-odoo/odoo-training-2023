# -*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class EstatePlan(models.Model):
    _name = "estate.property"
    _description = "This is Estate property model"
    #Table Fields
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode', required=True)
    date_availability = fields.Date(string='Date', copy=False, default= lambda self: fields.datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm.)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm.)')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    status = fields.Selection(
        string='State',
        selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        default= 'new'
    )
    active = fields.Boolean(string='Active', default=True)
    total_area = fields.Float(string="Total Area (sqm.)", compute="_compute_total")
    best_price = fields.Float(string="Best Offer", compute="_compute_best_offer")
    
    #Relational Fields
    property_type_id = fields.Many2one('estate.property.type',string="Property Type")
    buyer_id = fields.Many2one('res.partner',string="Buyer",copy=False)
    salesperson_id = fields.Many2one('res.users',string="Salesman", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag','property_tags_rel','prop_id','tag_id',string="Property Tags")
    offer_ids = fields.One2many('estate.property.offer','property_id')

    @api.depends("living_area","garden_area")
    def _compute_total(self):
            self.total_area = self.living_area + self.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'),default=0)

            
    @api.onchange("garden")
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation="north"
            else:
                record.garden_area = 0
                record.garden_orientation=""

    def action_sold_btn(self):
        for record in self:
            if record.status=='canceled':
                raise UserError('Cancelled property can\'t be sold.')
            record.status='sold'
        return True

    def action_cancel_btn(self):
        for record in self:
            if record.status=='sold':
                raise UserError('Sold Property can\'t be cancelled.')
            record.status='canceled'
        return True

    
        
            


    
    