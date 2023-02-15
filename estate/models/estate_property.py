from odoo import api,fields, models,exceptions
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    _sql_constraints = [
        ('check_expected_price', 
         'CHECK(expected_price>=0)',
         'The expected price must be positive.')
    ]

    name = fields.Char(required=True)
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description = fields.Text()
    postcode = fields.Char() 
    date_availability = fields.Date(copy=False,default=lambda self: fields.Datetime.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute = "_compute_garden_values",inverse = "_inverse_garden_values",store = True)
    garden_orientation = fields.Selection(
        compute = "_compute_garden_values",
        inverse = "_inverse_garden_values",
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Type is used to separate Leads and Opportunities",
        store = True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer received', 'Offer Received'), 
        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson",default=lambda self:self.env.user)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags", relation="tag_ids_m2m")
    offer_ids = fields.One2many("estate.property.offer","property_id", string="Offers")
    
    total_area = fields.Float(compute="_compute_total_area")
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Float(compute="_compute_best_price",store=True)
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                if(record.state == "new"):
                    record.state = "offer received"
                    record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0.0

            if(record.state == "offer received"):
                if(not record.offer_ids):
                    record.state = "new"

    @api.depends('garden')
    def _compute_garden_values(self):
        for record in self:
            if (record.garden == True):
                record.garden_area = 10
                record.garden_orientation = 'north'
            
            else:
                record.garden_area = 0
                record.garden_orientation = ''

    def _inverse_garden_values(self):
        for record in self:
            if ('record.garden_area != 0' and 'record.garden_orientation != ""'):
                record.garden = True
            
            else:
                record.garden = False
            
    def action_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise exceptions.UserError("Cancelled properties cannot be sold.")
            else: record.state = 'sold'

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("Sold properties cannot be cancelled.")
            else:record.state = 'cancelled'


