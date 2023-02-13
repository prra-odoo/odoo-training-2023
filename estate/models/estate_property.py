from odoo import models, fields
from dateutil.relativedelta import relativedelta


class RealEstate(models.Model):
    _name = "estate.property"
    _description = "This is a real estate module"
   

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string='Availability Date', default=lambda self: fields.Date.today()+relativedelta(months=+3), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(string='Selling Price',readonly=True , copy =False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
         string = 'Type',
        selection =[('N','North'),('E' , 'East'),('S','South'),('W','West')],
         help = 'Type is used to seprate directions'
    )
    active = fields.Boolean(String="Active", default = True)
    state = fields.Selection(
        selection=[
        ("new", "New"),
        ('offer_received','Offer Received'),
                     ('offer_accepted','Offer Accepted'),
                     ('sold','Sold'),
                     ('canceled','Canceled')
        ],
        string="State" ,default = "new",copy = False, required =True, 
    )