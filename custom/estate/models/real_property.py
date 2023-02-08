from odoo import models,fields
from datetime import datetime
from dateutil.relativedelta import relativedelta




class realProperty(models.Model):
    _name = "estate.real.property"
    _description = "Real estate model"
    name=fields.Char(default="unknown")
    description=fields.Char()
    postcode=fields.Char()
    date_availability=fields.Datetime(default=datetime.now() + relativedelta(months=3))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer(default="2")
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')],
        help="Select an appropriate direction")
    active=fields.Boolean()
    state=fields.Selection(string='State',
        selection=[('new','New'),('recieved','Offer Recieved'),('accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')],
        help="select the state")
    property_type=fields.Many2one("estate.property.type",name="Property Type")
    buyer=fields.Many2one("estate.property.type",name="Buyer",index=True, tracking=True, default=lambda self: self.env.user)
    seller=fields.Many2one("estate.property.type",name="Salesman",index=True, tracking=True, default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids=fields.One2many("estate.property.offer","partner_id",string="Offers")
    
    


    