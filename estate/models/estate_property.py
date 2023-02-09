from odoo import models, fields
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
    garden_area = fields.Integer()
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
