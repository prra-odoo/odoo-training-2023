# -- coding: utf-8 --

from odoo import fields,models,api
from dateutil.relativedelta import relativedelta
import datetime

TODAY = datetime.date.today()
three_mon_rel = relativedelta(months=3)

class estateProperty(models.Model):
    _name = "estate.property"
    _description="model description"

    name=fields.Char(string="Name",required=True)
    description=fields.Text(string="Description")
    postcode=fields.Char(string="Pin Code")
    date_availability=fields.Date(string="Availablity Date", default=TODAY + three_mon_rel)
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price")
    bedrooms=fields.Integer(string="Bedrooms", default=2)
    living_area=fields.Integer(string="Living Area")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(string="Garage")
    garden=fields.Boolean(string="Garden")
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection(
        string="Garden Orientation",
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])

    state = fields.Selection(
        string='Status',
        selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        default= 'new'
    )
    active=fields.Boolean(default=True)
    property_type_id=fields.Many2one("estate.property.type", string="Property type")
    tag_ids = fields.Many2many('estate.property.tags','property_and_tags_rel','prop_id','tag_id',string="Property Tags")
    buyer_id = fields.Many2one('res.partner',string="Buyer",copy=False)
    salesperson_id = fields.Many2one('res.users',string="Salesman", default=lambda self: self.env.user)

    offer_ids=fields.One2many("estate.property.offer", "property_id", string="Offers")    


    total_area=fields.Integer(compute="_compute_area")

    @api.depends("living_area","garden_area")
    def _compute_area(self):
        for record in self:
            record.total_area=record.living_area+record.garden_area






