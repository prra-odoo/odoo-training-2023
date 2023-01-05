from odoo import models,fields
from dateutil.relativedelta import relativedelta
class RealEstateProperty(models.Model):
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
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesman_id=fields.Many2one("res.users",string="Salesman")
    type_id=fields.Many2one("real.estate.property.type",string="Property Type")
    tags_id=fields.Many2many("real.estate.property.tags")
    offers_ids=fields.One2many("real.estate.property.offer","property_id",string="Offers")
class propertyType(models.Model):
    _name="real.estate.property.type"
    _description="Property Type"
    name=fields.Char(string='Property Type',required=True)
class propertyTags(models.Model):
    _name="real.estate.property.tags"
    _description="Property Tags"
    name=fields.Char(string="Property Tags",required=True)
class propertyOffer(models.Model):
    _name="real.estate.property.offer"
    _description="Property Offer"
    price=fields.Float()
    status=fields.Selection(selection=[("accepted","Accepted"),("refused","Refused")],copy=False)
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("real.estate.property",required=True)