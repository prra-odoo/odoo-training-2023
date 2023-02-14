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
    # refering other tables 
    buyer = fields.Many2one("res.partner", string="Buyer",copy=False)
    seller = fields.Many2one("res.users",string="Seller",default=lambda self: self.env.user)
    property_type_id = fields.Many2one("estate.property.type",string="Property Type",required=True)
    tag_ids = fields.Many2many("estate.property.tag",string="Property Tag",required=True)
    offer_ids = fields.One2many("estate.property.offer","property_id",string="")