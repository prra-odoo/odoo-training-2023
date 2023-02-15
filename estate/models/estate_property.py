from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

  

    name=fields.Char(required=True)
    description=fields.Char()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False, default= lambda self:(fields.Datetime.now().date()+relativedelta(months=+3)))

    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer(compute="_compute_garden")
    garden_orientation=fields.Selection(
        
        selection=[('E','East'),('W','West'),('N','North'),('S','South')],
        string="Garden Orientation",
        compute="_compute_garden"
        
    )

  
    state=fields.Selection(
        selection=[
            ('new','New'),
            ('offer_received','Offer Received'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled')
    
        ],
        string="Status",
        required=True,
        copy=False,
        default="new"
    )

    active=fields.Boolean("Active",default=True)

    total_area=fields.Integer(string="Total Area",compute="_compute_area")
    best_offer=fields.Float(string="Best Price",compute="_compute_best_offer")

    property_type_id=fields.Many2one('estate.property.type',string="Property Type")
    buyer_id=fields.Many2one('res.partner', string='Buyer',copy=False)

    salesperson_id=fields.Many2one('res.users',string="Salesman",default=lambda self:self.env.user)
    tag_ids=fields.Many2many('estate.property.tag',relation="tag_property")
    offer_ids=fields.One2many('estate.property.offer','property_id',string="Offer")



    @api.depends('living_area','garden_area')
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
              

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            if self.offer_ids:
                record.best_offer=max(self.offer_ids.mapped('price'))
            else:
                record.best_offer=0

    
    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_area=10
                record.garden_orientation="N"
            else:
                record.garden_area=False
                record.garden_orientation=False
           
