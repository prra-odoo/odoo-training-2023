from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "CRM Recurring revenue plans"

    name = fields.Char(required=True)
    description=fields.Char()   
    postcode = fields.Char(default="0")
    date_availability = fields.Date(readonly=True, default=lambda self:(fields.Datetime.now().date()+relativedelta(months=+3)))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    total_area=fields.Float(compute="_total_area",readonly=True)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    best_price = fields.Float(compute="_compute_discount")
    garden_orientation = fields.Selection(
        string='Type',
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help="Type is used to separate Directions"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection = [('new','New'),('off_re','Offer Received'),('off_ac','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        required=True,default="new",copy=False
    )

    property_type_id=fields.Many2one('estate.property.type',string="Property Type")
    property_tag_id=fields.Many2many('estate.property.tag',relation='property_tag_rel',string="Property Tag")
    offer_id=fields.One2many('estate.property.offer','property_id',string="Offer")


    buyers=fields.Many2one('res.partner',copy=False)
    salesmen=fields.Many2one('res.users',default=lambda self:self.env.user)

    @api.depends("living_area","garden_area")
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area


    @api.depends("offer_id")
    def _compute_discount(self):
        for record in self:
            if(record.offer_id): 
                record.best_price = max(record.offer_id.mapped("price"))
            else:
                record.best_price=0.0 
