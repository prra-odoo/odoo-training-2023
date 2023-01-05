# -*- coding: utf-8 -*-

from odoo import models , fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class estate_property(models.Model):
    _name = "estate.property"
    _description = "Advertisment module of real estate"
    active = fields.Boolean(default=True)
    _order = "id desc"
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)", "The expected price must be strictly positive"),
        ("check_selling_price", "CHECK(selling_price > 0)", "The selling price must be positive"),
    ]
    _inherit = ['mail.thread','mail.activity.mixin'] 
    
    
    
    name = fields.Char()
    postcode = fields.Integer(default = 104,readonly=True)
    description = fields.Text(copy=False)
    date_availability = fields.Date('Date Avilability',default=lambda self: fields.datetime.today()+relativedelta(months=6))
    expected_price = fields.Float(default = 550)
    selling_price=fields.Float(default = 50000)
    bedrooms = fields.Integer(default = 50)
    living_area = fields.Integer(default = 2)
    facades = fields.Integer(default = 5)
    garage = fields.Boolean(default= False)
    garden_area = fields.Integer(default = 1)
    total_area = fields.Float(compute="_compute_total_area")
    best_offer =  fields.Float(compute= "_compute_offer_price",default=0)
    Other_info = fields.Text("Others info")
    log_note=fields.Text("Log Note")
    garage_orientation = fields.Selection(
        string = 'Garage_Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    state = fields.Selection(
        string='Status',
        selection=[('new','New'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancel','Cancel')]
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property type")
    salesperson_id= fields.Many2one("res.users",string="Sales")
    buyers_id=fields.Many2one("res.partner",string="Buyers")
    tags_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer","property_id",string = "Property offer")
    # type_ids = fields.One2many("estate.property.type","property_id",string="Properites")
    
    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
        
    @api.depends('offer_ids.price')
    def _compute_offer_price(self):
        for record in self:
            record.best_offer = max(self.offer_ids.mapped('price'),default=0)
            
            
    def action_sold(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("Canceled properties cannot be sold")
            else:
                 record.state == 'sold'
        return True
            
    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold properties cannot be canceled")
            else:
                 record.state == 'cancel'
        return True
    @api.constrains("selling_price","expected_price")
    def _check_sellind_price(self):
        for record in self:
            if  float_compare(record.selling_price,0.9*record.expected_price,precision_digits =2) == -1:
                raise UserError("Selling Price must 90percent of the expected price")
    

              
    
            