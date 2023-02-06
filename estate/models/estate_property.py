from odoo import models, fields
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
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
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
    