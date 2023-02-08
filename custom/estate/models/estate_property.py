
from odoo import models,fields  
from dateutil.relativedelta import relativedelta
class EstateProperty(models.Model):
    _name="estate.property"
    _description="estate property project"
    name=fields.Char(required=True)
    active=fields.Boolean(default=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(default=lambda self:fields.Date.today()+relativedelta(months=3),copy=False)
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
        string='Type',
        selection=[('N','North'),('S','South'),('E','East'),('W','West')],
        help="Choose direction"
    )
    state=fields.Selection(
        string='State',
        selection=[('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        default='new',
        required=True
    )
    property_type_id=fields.Char()