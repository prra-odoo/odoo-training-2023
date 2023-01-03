from odoo import models,fields
from dateutil.relativedelta import relativedelta
class property(models.Model):
    _name='real.estate.property'
    _description="Property model"
    name=fields.Char(string='Property Name',required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(default=fields.Datetime.now()+relativedelta(months=3))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer()
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(selection=[('north','North'),('south','South'),('east','East'),('west','West')])
    active=fields.Boolean(default=True)
    state=fields.Selection(selection=[('new','New'), ('offer_received','Offer Received'), ('offer_accepted','Offer Accepted'), ('sold','Sold'),('canceled','Canceled')],default='new')