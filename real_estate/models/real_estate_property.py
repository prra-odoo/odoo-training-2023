from odoo import fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta

# six_months_after  = datetime.now() + relativedelta(months=2)


class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Property Model"

    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        default=datetime.now() + relativedelta(months=3))
    # date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    # expected_price = fields.Float('Expected Price', index=True,required=True)
    selling_price = fields.Float()
    # selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], default="north")
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted',
                             'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], default='new', required=True, copy=False)
    property_type_id = fields.Many2one(
        'real.estate.property.type', string='Property Type')
    salesperson_id = fields.Many2one(
        "res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("real.estate.property.tags")
    offer_ids = fields.One2many(
        "real.estate.property.offer", "property_id", string="Offers")
    tatal_area = fields.Float(compute="_compute_total_area")

    # @api.depends(living_area)
    # def _compute_total_area(self):
    #     for record in self:
    #         record.total = 2.0 * record.amount
