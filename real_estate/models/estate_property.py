from odoo import fields,models
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "CRM Recurring revenue plans"

    name = fields.Char(required=True)
    description=fields.Char()   
    postcode = fields.Char(default="0")
    date_availability = fields.Date(readonly=True, default=lambda self:(fields.Datetime.now().date()+relativedelta(months=+3)))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help="Type is used to separate Directions"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection = [('new','New'),('off_re','Offer Received'),('off_ac','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        required=True,default="new",copy=False
    )



