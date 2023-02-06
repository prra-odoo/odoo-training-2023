from odoo import models,fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

  

    name=fields.Char(required=True)
    description=fields.Char()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False, default= datetime.now() + relativedelta(months=3))

    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
        
        selection=[('E','East'),('W','West'),('N','North'),('S','South')],
        string="Garden Orientation"
        
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

    active=fields.Boolean("Active",default=False)