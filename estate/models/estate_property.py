from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is an Estate Model"
    _order = "id desc"

    _sql_constraints = [
        ('exp_price_pos', 'CHECK(expected_price >= 0)',
         'The expected price must be greater than 0.'),
        ('sell_price_pos', 'CHECK(selling_price >= 0)',
         'The selling price must be greater than 0.'),
    ]
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, default="Unknown Estate")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        string='Available From', copy=False, default=lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(required=True, default=100)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(default=False)

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
        copy=False,
        default='N',
        tracking=True
    )

    property_type_id = fields.Many2one(
        comodel_name="estate.property.type", string="Property Type", tracking=True)

    salesman_id = fields.Many2one(
        comodel_name='res.users', string="Salesman", default=lambda self: self.env.user)

    buyer_id = fields.Many2one(
        comodel_name='res.partner', string="Buyer", copy=False, tracking=True)

    tag_ids = fields.Many2many(
        comodel_name="estate.property.tag", string="Tags", copy=False, tracking=True)

    offer_ids = fields.One2many(
        comodel_name="estate.property.offer", inverse_name="property_id", store=True, tracking=True)

    total_area = fields.Float(compute='_compute_total_area')

    best_price = fields.Float(compute='_compute_best_price')

    garden_area = fields.Integer(
        compute="_compute_garden_area", string='Garden Area (sqm)',
        inverse="_inverse_garden_area", store=True)

    is_favorite = fields.Boolean()

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area+record.living_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if (record.offer_ids):
                # Whenever a new offer is created, state changes to "OR".
                # --> Already implemented by overriding create method in estate_property_offer.
                # if (record.state == "N"):
                #     record.state = "OR"
                amount = max(record.mapped('offer_ids.price'))
                record.best_price = amount
            else:
                # To mark the property as new when all the offers are deleted.
                # --> Done in estate_property_offer as mark_new_no_offer.
                # if (record.state in ["OR", "OA", "S", "C"]):
                #     record.state = 'N'

                # To reset the selling price if an already accepted offer has been deleted.
                record.selling_price = 0
                record.buyer_id = False
                record.best_price = 0

    @api.depends("garden")
    def _compute_garden_area(self):
        # print("------------------------CoMpUtE---------------------------------")
        # With store=True enabled, this function won't recompute the values when user
        # has changed the values manually, while garden is True.
        for record in self:
            if (record.garden):
                record.garden_area = 10
                record.garden_orientation = "N"
            else:
                record.garden_area = 0
                record.garden_orientation = False

    def _inverse_garden_area(self):
        # The only use of this function is to reset the values when user has changed some
        # values in garden area and orientation and saves when garden = False.
        # print("---------------------Inverse-------------------------------")
        for record in self:
            if (not record.garden):
                record.garden_area = 0
                record.garden_orientation = False

    def btn_sold(self):
        for record in self:
            if (record.state in ["N", "OR"]):
                raise UserError(
                    _('Properties can only be sold after accepting an offer.'))
            elif (record.state == "OA"):
                record.state = 'S'
            elif (record.state == "C"):
                raise UserError(
                    _('Cancelled Properties cannot be sold.'))

    def btn_cancel(self):
        for record in self:
            if (record.state in ["OR", "OA"]):
                record.state = 'C'
            else:
                raise UserError(
                    _('Already sold properties cannot be cancelled.'))

    @api.constrains("selling_price")
    def check_selling_price(self):
        for record in self:
            if (record.selling_price > 0):
                desired_sell_price = 0.9*record.expected_price
                check_sell_price = float_compare(
                    desired_sell_price, record.selling_price,  precision_digits=2)
                # desired_sell_price >,=,< record.selling_price => [1,0,-1]
                # here we need record.selling_price > desired_sell_price, therefore -1.
                if (check_sell_price >= 0):
                    raise ValidationError(
                        "Selling Price must be greater than 90% of the expected price.")

    @api.ondelete(at_uninstall=False)
    def _unlink_except_new_cancel(self):
        for rec in self:
            if (rec.state not in ["N", "C"]):
                raise UserError(
                    _('You can only delete properties that are not new or cancelled.'))
