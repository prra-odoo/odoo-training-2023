from odoo import api, models, fields
from dateutil.relativedelta import relativedelta


class EstatePropertyModel(models.Model):
    _name = "estate.property"
    _description = "this is the Estate Property Model"

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
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'), ('west', 'West')],
        help="Type is used to show direction"
    )
    selling_price = fields.Integer(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    date_availability = fields.Date(default=lambda self: (fields.Datetime.today(
    )+relativedelta(months=+3)), copy=False, string="Available From")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancled', 'Cancled')],
        default="new",
        required=True,
        copy=False
    )
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    salesperson = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', index=True)
    tag_ids= fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer','property_id',)
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")

    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                record.best_price=max(record.offer_ids.mapped("price"))
            else:
                record.best_price=0.0