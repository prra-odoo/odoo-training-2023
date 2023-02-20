from odoo import fields,models,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import UserError,ValidationError
from odoo.tools.float_utils import float_compare,float_is_zero
 
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a real-estate property model"
    _order="id desc"
    _sql_constraints=[
         ('check_expected_price',
         'CHECK(expected_price > 0)',
         'Expected price should be positive and greater than 0'),
         ('check_selling_price',
        'CHECK(selling_price>0)',
        'Selling price should be positive and greater than 0')
    ]


    name = fields.Char(string= 'Title',required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string= 'Available From',copy=False, default= datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)',compute="_compute_value", store=True, readonly=False)
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Choose appropriate direction",
        compute="_compute_value", store=True, readonly=False
    )       

    active=fields.Boolean('Active', default=True)
    state = fields.Selection(
     string='state',
     selection=[('new', 'New'),('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
     required=True, 
     copy=False,
     default='new' 
    )

    property_type_id=fields.Many2one("estate.property.type", string = "Property Type")
    seller_id=fields.Many2one('res.users',string='Salesman', default=lambda self: self.env.user)
    buyer_id=fields.Many2one('res.partner',string='Buyer',copy=False)
    tags_ids=fields.Many2many('estate.property.tags')
    offer_ids=fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_id',
        string='Offers')
    total_area=fields.Float(compute="_compute_total_area")
    best_price=fields.Float(compute="_compute_best_price")
   

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                record.best_price=max(record.offer_ids.mapped('price'))
            else:
                record.best_price=0.0

    @api .depends("garden")
    def _compute_value(self):
      for record in self : 
        if (record.garden==True):
            record.garden_area=10
            record.garden_orientation="north"
        else:        
            record.garden_area=0
            record.garden_orientation=''

    def action_sold(self):
        for record in self:
            if (record.state=="canceled"):
               raise UserError("Canceled properties cannot be sold")  
        else:
            record.state="sold"            
        return True  
            

    
    
    
    def action_canceled(self):
        for record in self:
            if (record.state=="sold"):
             raise UserError("Sold properties cannot be canceled")  
        else:
            record.state="canceled"        
        return True
    
    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for record in self:
            if not float_is_zero(record.selling_price,precision_digits=2):
                if float_compare(record.selling_price,record.expected_price*0.9,precision_digits=2)<=0:
                    raise ValidationError("Selling price should not be lower than 90% the expected price")

 

                

