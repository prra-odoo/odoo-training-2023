from odoo import models,fields,api
from datetime import datetime
from dateutil.relativedelta import relativedelta




class realProperty(models.Model):
    _name = "estate.real.property"
    _description = "Real estate model"
    name=fields.Char(default="unknown")
    description=fields.Char()
    postcode=fields.Char()
    date_availability=fields.Datetime(default=datetime.now() + relativedelta(months=3))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer(default="2")
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')],
        help="Select an appropriate direction")
    active=fields.Boolean()
    state=fields.Selection(string='State',
        selection=[('new','New'),('recieved','Offer Recieved'),('accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')],
        help="select the state")
    property_type_id=fields.Many2one("estate.property.type",name="Property Type")
    buyer_id=fields.Many2one("res.partner",name="Buyer",copy=False)
    seller_id=fields.Many2one("res.users",name="Salesman", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags", relation='tag_ids_m2m')
    offer_ids = fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_id',
        string='Offers',
        required=True        
    )
    total_area=fields.Float(compute='_compute_total')
    @api.depends('garden_area','living_area')
    def _compute_total(self):
        for record in self:
            record.total_area=record.garden_area+record.living_area
    description_buyer=fields.Char(compute='_compute_description_buyer')
    @api.depends('buyer_id.name')
    def _compute_description_buyer(self):
        for record in self:
             record.description_buyer= record.buyer_id.name
    best_price=fields.Float(compute='_compute_best_price')
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                record.best_price=max(record.offer_ids.mapped("price"))
            else:
                record.best_price=0.0
    @api.onchange('garden')
    def onchange_check_garden(self):
        if self.garden==True:
            self.garden_area=10
            self.garden_orientation='north'
        else:
            self.garden_area=0
            self.garden_orientation=""

           



    