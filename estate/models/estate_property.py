from odoo import models,fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Model"

    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    postcode = fields.Char()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default='2')
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()   
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Select your direction!",default="north")
    active = fields.Boolean(default=True,required=True  )
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer received', 'Offer Received'), 
        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesman_id = fields.Many2one("res.partner", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.users", string="Buyer",copy=False)
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    

