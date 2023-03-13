from odoo import api, models, fields
from dateutil.relativedelta import relativedelta
from odoo import exceptions
from odoo.tools.float_utils import float_compare, float_is_zero


class EstatePropertyModel(models.Model):
    _name = "estate.property"
    _description = "this is the Estate Property Model"
    _sql_constraints = [
        (
            'check_expected_price',
            'CHECK(expected_price>0)',
            'Expected price should be positive and greater than 0'
        )
    ]
    _order="id desc"

    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(default=False)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'), ('west', 'West')],
        help="Type is used to show direction"
    )
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    date_availability = fields.Date(default=lambda self: (fields.Datetime.today(
    )+relativedelta(months=+3)), copy=False, string="Available From")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        default="new",
        required=True,
        copy=False
    )
    property_type_id = fields.Many2one(
        'estate.property.type', string="Property Type")
    salesperson = fields.Many2one(
        'res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', index=True, readonly=True)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")
    cancel_btn = fields.Boolean(default=False)
    sold_btn = fields.Boolean(default=False)

    def action_set_sold(self):
        for record in self:
            # record.sold_btn=True
            if record.state == 'canceled':
                raise exceptions.UserError("Canceled Property cannot be Sold")
            else:
                record.state = 'sold'

    def action_set_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("Sold property cannot be Canceled")
            else:
                record.state = 'canceled'

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if (record.offer_ids):
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0

    @api.onchange("garden")
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 100
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0
                record.garden_orientation = ''

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if not float_is_zero(record.expected_price, precision_digits=2) and not float_is_zero(record.selling_price, precision_digits=2):
                if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
                    raise exceptions.ValidationError("Selling price cannot be lower than 90 percent of the expected price!")
                
    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_canceled(self):
        for record in self:
            if record.state not in ['new','canceled']:
                raise exceptions.UserError("Only new and canceled properties can be deleted")
