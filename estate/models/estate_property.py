# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import date
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string = "Name", required = True, help = "this is name")
    description = fields.Text(string = "Description")
    postcode = fields.Char(string = "Pin Code", required = True)
    date_availability = fields.Date(string = "Availablity Date",copy = False,default = (date.today() + relativedelta(months=+3)))
    expected_price = fields.Float(string = "Expected Price", required = True)
    selling_price = fields.Float(string = "Selling Price",readonly = True,copy = False)
    bedrooms = fields.Integer(string = "Bedroom Number",default="2")
    living_area = fields.Integer(string = "Living Area")
    facades = fields.Integer(string = "Facades")
    garage = fields.Boolean(string = "Garage")
    garden = fields.Boolean(string = "Garden")
    garden_area = fields.Integer(string = "Garden Area")
    garden_orientation = fields.Selection(
        string = "Garden Orientation",
        selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(string = "Active",default=True)
    state = fields.Selection(
        string = "State",
        tracking=True,
        selection = [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancel', 'Canceled')],
        default='new')
    salesperson_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner',string='Buyer',copy=False)
    property_type_id= fields.Many2one("estate.property.type",string="Property Type")
    tags_ids= fields.Many2many("estate.property.tags",'property_under_tag_rel', 'property_id', 'tag_id',string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total_area",string="Total Property Area")
    best_offer = fields.Float(compute="_compute_best_offer",string="Best Offer")


    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped("price"),default=0)
    
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden==True:
            self.garden_orientation ='north'
            self.garden_area = "10"
            return {'warning': {
                'title': _("Rich Alert"),
                'message': ('House with gardens u richie rich :) ')}}
        if self.garden==False:
            self.garden_orientation =''
            self.garden_area = ""
        
    def sold_buisness_logic(self):
        if self.state!='cancel':
            self.state='sold'
            return True
    
    def cancel_buisness_logic(self):
        if self.state!='sold':
            self.state='cancel'
            return True
