from odoo import fields,models
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
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
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