from odoo import models,fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last seen",default = lambda self : fields.Datetime().now())
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Available from",default = lambda self : fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[("north","North"),("south","South"),("east","East"),("west","West")])
    active = fields.Boolean(default = False)
    status = fields.Selection(selection=[("new","New"),("offer received","Offer Received"),("offer accepted","Offer Accepted"),("sold","Sold"),("canceled","Canceled")],default = "New",copy = False)