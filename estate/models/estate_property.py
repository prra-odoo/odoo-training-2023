from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):

    _name = "estate.property"
    _description = "estate property detailed field"
    
    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char(default="0")
    # default=datetime.datetime.now().date()+datetime.timedelta(days=90)
    date_availability = fields.Date(readonly=True,default=lambda self:(fields.Datetime.now().date()+relativedelta(months=+3)))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Float()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Float()
    garden_orientation = fields.Selection(
        string = "Direction",
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help  = "Select Direction"
        )
         
    active = fields.Boolean("Active",default=True)
    state = fields.Selection(
        string = "Status",
        selection = [('new','New'),('received','Offer Received'),('accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        help  = "Status",
        default = "new",
        copy=False
        )
    
    property_type_id = fields.Many2one('estate.property.type',string="Property Type")
    property_tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    offer_ids = fields.One2many('estate.property.offer',"property_id",string="Offers")
    
    buyer = fields.Many2one('res.partner',copy=False)
    salesmans = fields.Many2one('res.users', default=lambda self:self.env.user)

    total_area = fields.Float(string='Total Area', readonly=True, compute = "_compute_total_area")

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Float(compute = "_compute_best_offer" ,string="Best Price", readonly=True)

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for record in self:
            if(record.offer_ids):
                record.best_price = max(record.offer_ids.mapped('price'))
            else: 
                record.best_price = 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north' 
        else:
            self.garden_area = 0
            self.garden_orientation = '' 
