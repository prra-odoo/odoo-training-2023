# -*- coding: utf-8 -*-

from odoo import models , fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare,float_is_zero

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
    
    
    
    name = fields.Char(required=True)
    postcode = fields.Integer()
    description = fields.Text(copy=False)
    date_availability = fields.Date('Date Avilability',default=lambda self: fields.datetime.today()+relativedelta(months=3))
    expected_price = fields.Float(default= 100)
    selling_price=fields.Float(default = 100000)
    bedrooms = fields.Integer(default = 50)
    living_area = fields.Integer(default = 2)
    facades = fields.Integer(default = 5)
    garage = fields.Boolean(default= False)
    garden_area = fields.Integer("Garden area(sqm)", tracking = True)
    total_area = fields.Float(compute="_compute_total_area")
    best_offer =  fields.Float(compute= "_compute_offer_price",default=0)
    sequence = fields.Integer("sequence")
    other_info = fields.Text("Other Information")
    garage_orientation = fields.Selection(
        string = 'Garage_Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    state = fields.Selection(
        string='Status',
        selection=[('new','New'),('offer_received','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancel','Cancel')],
        default="new",
        tracking = True
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property types")
    salesperson_id= fields.Many2one("res.users",string="Sales")
    buyers_id=fields.Many2one("res.partner",string="Buyers")
    tags_ids = fields.Many2many("estate.property.tag",required=True,string="Tags")
    offer_ids = fields.One2many("estate.property.offer","property_id",string = "Property offer")
    country_id = fields.Many2one("res.country",string="Country")
    
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
                 record.state ='sold'
        return True
            
    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold properties cannot be canceled")
            else:
                record.state ='cancel'
        return True
    
    @api.constrains("selling_price","expected_price")
    def _check_selling_price(self):
        for record in self:
            if (
                not float_is_zero(record.selling_price, precision_rounding=0.01)
                and float_compare(record.selling_price, record.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0
            ):
              
                raise UserError("Selling Price must 90percent of the expected price")
        
    # def unlink(self):
    #     for record in self:
    #         if record.state not in {'new','cancel'}:
    #             raise UserError("Only new and canceled properties can be deleted")
    #     return super().unlink()
    

              
    
            