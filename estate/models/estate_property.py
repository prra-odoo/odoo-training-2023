from odoo import models,fields
from datetime import date
from dateutil.relativedelta import relativedelta

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
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='type',
        selection=[('lead','Lead'),('opportunity','Opportunity')],
        help="Type is used to separate Leads and Opportunities"
        )
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new','New'),
        ('offer received','Offer Received'),
        ('offer accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')
    ],
    default='new',
    )