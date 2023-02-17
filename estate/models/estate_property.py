from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "It's a estate prooperty module"
    
    name = fields.Char(required=True,string='Title')
    description = fields.Char()
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(default = date.today() + relativedelta(months=+3),copy=False)
    expected_price = fields.Float(required=True,string='Expected Price')
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default = 2,string='Bedrooms')
    living_area = fields.Float(string='Living Area (sqm)',default=100)
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)',default=10)
    garden_orientation = fields.Selection(
        string='Garden Orentation',
        selection=[
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')
        ],
        default = 'north'
        )
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new','New'),
        ('offer_received','offer received'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')
    ],
    default='new',
    )
    

    # Relationals Fields
    buyer_id = fields.Many2one("res.partner", string="Buyer",copy=False)
    seller_id = fields.Many2one("res.users",string="Seller",default=lambda self: self.env.user)
    property_type_id = fields.Many2one("estate.property.type",string="Property Type",required=True)
    tag_ids = fields.Many2many("estate.property.tag",string="Property Tag",required=True)
    offer_ids = fields.One2many("estate.property.offer","property_id")

    # computed fields
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute = "_compute_best_price",default=0)

    # Compute method for calculating total area
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            # print("------------------------------", self.name)
            record.total_area = record.living_area + record.garden_area
        # print("------------------------------", self.name)     
        # self.total_area = self.living_area + self.garden_area 
       
    # compute method for best offer
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price"),default=0)
            if record.offer_ids:
                record.state = "offer_received"
            
        
    # @api.depends("offer_ids")
    # def _compute_state(self):
    #     for record in self:
    #         if record.offer_ids:
    #             record.state = "offer_received"
    # Action methods
    def action_set_state_sold(self):
        for record in self:
            if record.state == "canceled":
                raise UserError("Can't set canceled property to sold")
            else:
                record.state = "sold"
        return True
    
    def action_set_state_cancel(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Can't set sold property to cancel")
            else:
                record.state = "canceled"
        return True   
