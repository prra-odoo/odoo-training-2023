from odoo import models,fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    
    _name = "estate.property"
    _description = "Real Estate Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    #date_availability = fields.Date(default=fields.Datetime.today())
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False,string="Available from")
    #if date is used then Date.today() and if Datetime is used then Datetime.now()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer accepted', 'Offer Accepted'), ('offer recieved', 'Offer Recieved'), ('sold', 'Sold'),('cancelled','Cancelled')],
        help="Select your state!",
        required=True,
        default="new",
        copy=False
        )
    garden_orientation = fields.Selection(
        string='Direction',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Select your direction!"
        )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner',string="Buyer",copy=False)
    seller_id = fields.Many2one('res.users',string="Seller", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag",string="Property Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")