from odoo import models,fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property advertisment"

    name = fields.Char(required=True, string="Title")
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float(required=True)
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.today()+relativedelta(months=3))
    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    garden = fields.Boolean()
    garden_orientation = fields.Selection(
        string = "Garder Orientation",
        selection = [('north','North'),('South','South'),('East','East'),('West','West')],
        help = "Choose the direction"
    )
    selling_price = fields.Float(readonly=True, copy=False)
    living_area = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    state = fields.Selection(
        string = "State", 
        default = 'offer received',
        selection = [('new','New'),('offer received','Offer Received'),('sold','Sold'),('canceled','Canceled')],
        help = "Choose the direction",
        required = True,
        copy = False
    )

