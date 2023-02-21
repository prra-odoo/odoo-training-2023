from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError


class TestModel(models.Model):
    _name="estate.property"
    _description = "Testing an Estate Module"
    _order="id desc"

    name = fields.Char(required=True,default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default= lambda self: fields.Datetime.now()+relativedelta(month=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(compute="_compute_garden_field",readonly=False,store=True)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north','North'), ('south','South'), ('east','East'), ('west','West')],
        compute='_compute_garden_fields',
        help = 'Select one from Below ', 
        store=True,
        readonly=False,)
    state = fields.Selection(
        selection = [('new','New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'),
                      ('sold', 'Sold'), ('canceled', 'Canceled')  ],
                      default='new')
    active = fields.Boolean(default=True)
    # Linking Others Modules
    property_type_ID= fields.Many2one('estate.property.type',string="estate_type_partner")
    buyer_id=fields.Many2one('res.partner')
    salesperson_id = fields.Many2one('res.users', default= lambda self : self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="estate_tags")
    offer_ids = fields.One2many('estate.property.offer',"property_id")
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer= fields.Integer(compute="_compute_best_offer")

    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area= record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            if(record.offer_ids):
                # record.offer_ids.mapped('price')   Different  way of doing 
                record.best_offer = max(offer.price for offer in record.offer_ids)                           
            else:
                record.best_offer = 0

    @api.depends("garden")
    def _compute_garden_fields(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0
                record.garden_orientation = None


    def sold_action_button(self):
        if self.state == "canceled":
            raise UserError('Cancelled properties cannot be sold.')

    def cancel_action_button(self):
        if self.state == "sold":
            raise UserError("Sold property cant't be cancelled")



    # _sql_constraints=[(
    #     'expected_price_check',
    #     'CHECK(expected_price>0)',
    #     'Expected Price Must Be Strongly Positive')]

    _sql_constraints=[(
        'selling_price_positive','CHECK(selling_price>0)',
        'Selling price Must be Positive')]

    _sql_constraints = [
        ('check_expected_price',
        'CHECK(expected_price > 0)',
        'Expected Price Must be Positive')
    ]
    

    @api.constrains('selling_price')
    def find_selling_price(self):
        # breakpoint()
        for record in self:
            ten=record.expected_price*10/100
            actual=record.expected_price-ten
            if record.selling_price <actual:
                raise ValidationError("Selling price is not close to expected price")
            else:
                pass
