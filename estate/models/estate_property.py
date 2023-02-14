from odoo import fields,models,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
 
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a real-estate property model"

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
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Choose appropriate direction"
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
    tags_id=fields.Many2many('estate.property.tags')
    offer_ids=fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_id',
        string='Offers')
    total_area=fields.Float(compute="_compute_total")
    best_price=fields.Float(compute="_compute_best_price")


    @api.depends('living_area','garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area=record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for best_price in self:
            if(best_price.offer_ids):
                best_price.best_price=max(best_price.offer_ids.mapped('price'))
            else:
                best_price.best_price=0.0















