from odoo import api,models,fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property advertisment"

    name = fields.Char(required=True, string="Title")
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float(required=True)
    date_availability = fields.Date(copy=False, string="Available From", default=lambda self: fields.Date.today()+relativedelta(months=3))
    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    garden = fields.Boolean()
    garden_orientation = fields.Selection(
        string = "Garden Orientation",
        selection = [('north','North'),('South','South'),('East','East'),('West','West')],
        help = "Choose the direction"
    )
    tag_id = fields.Many2many("estate.property.tag", string="Tags")
    property_type_id = fields.Many2one("estate.property.type")
    buyer = fields.Many2one("res.partner", copy=False)
    seller = fields.Many2one("res.users", default=lambda self: self.env.user)
    selling_price = fields.Float(readonly=True, copy=False)
    garage = fields.Boolean()
    state = fields.Selection(
        string = "State", 
        default = 'offer received',
        selection = [('new','New'),('offer received','Offer Received'),('sold','Sold'),('canceled','Canceled')],
        help = "Choose the direction",
        required = True,
        copy = False
    )

    total_area = fields.Integer(compute="_compute_total")
    garden_area = fields.Integer()
    living_area = fields.Integer()
    @api.depends("living_area","garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    best_price = fields.Float(compute="_compute_best_price")
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0