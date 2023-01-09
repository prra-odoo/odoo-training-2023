from odoo import models,fields,api
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
    tags_ids=fields.Many2many("real.estate.property.tags")
    offers_ids=fields.One2many("real.estate.property.offer","property_id",string="Offers")
    total_area=fields.Integer(compute="_compute_total_area",inverse="_inverse_total_area")
    best_offer=fields.Float(compute="_compute_best_offer")
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.living_area+record.garden_area
    def _inverse_total_area(self):
        for record in self:
            record.living_area=record.total_area-record.garden_area
    @api.depends("offers_ids")
    def _compute_best_offer(self):
        for record in self:
            offer=record.offers_ids.mapped('price')
            if offer:
                record.best_offer=max(offer)
            else:
                record.best_offer=0
    @api.onchange("garden")
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area=10
                record.garden_orientation='north'
            else:
                record.garden_area=0
                record.garden_orientation=''