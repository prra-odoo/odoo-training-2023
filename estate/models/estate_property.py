# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class Estate_Property(models.Model):
    _name = "estate.property"
    _description = "Property Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)", "The expected price must be strictly positive"),
        ("check_selling_price", "CHECK(selling_price >= 0)", "The offer price must be positive"),   
    ]
    _order = "id desc"

    name = fields.Char(string = 'name',required=True)
    image = fields.Image("Logo", max_width=128, max_height=128)
    description = fields.Text(string = 'description')
    postcode = fields.Char(string = 'postcode', required = True)
    data_avabilability = fields.Date('Datetime',default=fields.Date.today()+relativedelta(months=3), copy=False)
    expected_price = fields.Float(string = 'expected price',required = True)
    selling_price = fields.Float(string = 'selling price', copy=False)
    bedrooms = fields.Integer(string = 'bedrooms' ,default=2)
    living_area = fields.Integer(string = 'living area')
    facades = fields.Integer(string = 'facades')
    garden = fields.Boolean(string ="Garden")
    garage = fields.Boolean(string = 'garage')
    garden_area = fields.Integer(
        string = 'garden area',
        compute="_compute_garden_area",
        readonly=False,
        store=True)
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')],
        compute="_compute_garden_area",
        readonly=False,
        store=True,
    )
    state = fields.Selection(
        string = 'State',
        tracking=True,
        default="new",
        copy=False,
        selection = [('new','New'),
        ('offer_received','Offer Received'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')]
    )
    active = fields.Boolean("Active", default=False)

    tag_ids = fields.Many2many("estate.property.tag","estate_property_rel","property_id","property_tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer",'property_id',string="Offer")
    
    total_area = fields.Integer(string ='Total area', compute = "_compute_total_area")
    best_price = fields.Float(string ='Best Offer', compute = "_compute_best_price")

    property_type_id = fields.Many2one("estate.property.type", string = 'Property Type',)
    user_id = fields.Many2one('res.users', string='Salesperson',default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner',string = 'Buyer',copy=False)

    # company_id=fields


    #compute method('garden_orientation', 'in', ['north','south'])
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    #best offer
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price"),default=0) 

    #onchange done with the help of compute field
    @api.depends("garden")
    def _compute_garden_area(self):
        for record in self:
            if record.garden==True:
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0  
                record.garden_orientation= ''  

    #buttons for sold and cancelation of the property
    def action_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("A canceled property cannot be sold")
            else:
                record.state = 'sold'
            
    def action_cancle(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("A sold property cannot be Canceled")
        else:
            record.state = 'canceled'
            

    #python constrains         
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < .9*record.expected_price:
                raise ValidationError("The selling price cannot be less than 90 percent of the expected price")
    
    #python inheritance
    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_cancle(self):
        if self.state not in ['new','canceled']:
            raise UserError("Only new and canceled properties can be deleted.")


        




