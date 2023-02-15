from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is an Estate Model"

    name = fields.Char(required=True, default="Unknown Estate")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        string='Available From', copy=False, default=lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()

    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('N', 'North'), ('S', 'South'),
                   ('E', 'East'),  ('W', 'West')],
        help="Select an appropriate direction")

    last_seen = fields.Datetime(
        string="Last Seen", default=lambda self: fields.Datetime.now())

    active = fields.Boolean(string='ACTIVE', default=True)

    state = fields.Selection(
        string='State of offer',
        selection=[('N', 'New'), ('OR', 'Offer Recieved!'),
                   ('OA', 'Offer Accepted!'), ('S', 'Sold'), ('C', 'Cancelled')],
        help="Deal Status to be provided here...",
        required=True,
        copy=False,
        default='N'
    )

    property_type_id = fields.Many2one(
        comodel_name="estate.property.type", string="Property Type")

    salesman_id = fields.Many2one(
        'res.users', string="Salesman", default=lambda self: self.env.user)

    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)

    tag_ids = fields.Many2many(
        comodel_name="estate.property.tag", string="Tags", copy=False)

    offer_ids = fields.One2many(
        comodel_name="estate.property.offer", inverse_name="property_id")

    total_area = fields.Float(compute='_compute_total_area')

    best_price = fields.Float(compute='_compute_best_price')

    garden_area = fields.Integer(compute="_compute_garden_area",
                                 inverse="_inverse_garden_area", string='Garden Area (sqm)')

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area+record.living_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if (len(record.offer_ids.mapped('price')) > 0):
                amount = max(record.mapped('offer_ids.price'))
                record.best_price = amount
            else:
                record.best_price = 0

    flag = True

    @api.depends("garden")
    def _compute_garden_area(self):
        for record in self:
            if (record.garden):
                record.garden_area = 10
                record.garden_orientation = "N"
            else:
                pass

    def _inverse_garden_area(self):
        for record in self:
            record.garden_area = 99
