from odoo import models,fields
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name = "estate.property"
    _description = "Real Estate Model"

    name = fields.Char(required=True,default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default='2')
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()   
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Direction',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Select your direction!",default="north")
    active = fields.Boolean(default=True,required=True  )
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer received', 'Offer Received'), 
        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False)

    

