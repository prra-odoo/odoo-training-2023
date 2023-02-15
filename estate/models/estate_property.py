from odoo import models,fields,api,exceptions
from dateutil.relativedelta import relativedelta
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateProperty(models.Model):
    
    _name = "estate.property"
    _description = "Real Estate Model"
    _sql_constraints = [
        ('expected_price', 'CHECK(expected_price >= 0)',
         'The expected price should be a positive number only.'),
         ('selling_price', 'CHECK(selling_price >= 0)',
         'The selling price should be a positive number only.')

    ]

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    #date_availability = fields.Date(default=fields.Datetime.today())
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False,string="Available from")
    #if date is used then Date.today() and if Datetime is used then Datetime.now()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute='_compute_garden_values',store=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'),  ('offer received', 'Offer Received'),('offer accepted', 'Offer Accepted'), ('sold', 'Sold'),('cancelled','Cancelled')],
        help="Select your state!",
        required=True,
        default="new",
        copy=False
        )
    garden_orientation = fields.Selection(
        string='Direction',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Select your direction!",
        compute='_compute_garden_values',
        store=True
        )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type",required=True)
    buyer_id = fields.Many2one('res.partner',string="Buyer",copy=False)
    seller_id = fields.Many2one('res.users',string="Seller", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag",string="Property Tag",relation="many2many_aman_tags_relation",column1="property_id",column2="property_tag_id")
    # in many2many a new table (rel) is created and data is stored in that and name of that model is firstModel_id secondModel
    #  my_field = fields.Many2many('other.model', 'My Field', model_name='my.model.other')model_name is used to change the newly created model
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    # one2Many(comodel name, inverse name)    
    total_area = fields.Integer(compute="_total_area",store=True)
    # @ depends - decorators (if we dont write @api line then compute works but only after save.)
    @api.depends('living_area','garden_area')
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_offer = fields.Float(compute='_compute_best_offer',store=True)
    # @api.depends("offer_ids")
    # def _best_offer(self):
    #     for record in self:
    #         if(record.offer_ids):
    #             if(record.state == "new"):
    #                 record.state = "offer recieved"
    #                 record.best_offer=max(record.offer_ids.mapped("price"))
    #         else:
    #             record.best_offer=0.0
    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            if(record.offer_ids):
                if(record.state == "new"):
                    record.state = "offer received"
                    record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0.0

            if(record.state == "offer received"):
                if(not record.offer_ids):
                    record.state = "new"
    # onchange function when garden field is enabled
    # compute field is not stored in DB by default
    @api.depends('garden')
    def _compute_garden_values(self):
        for record in self:
            if (record.garden==True):
                record.garden_area = 10.0
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0.0
                record.garden_orientation = False
            

    #function making two button of sold and cancelled in header
    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("sold property can't be cancelled.")
            else:record.state = 'cancelled'
    def action_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise exceptions.UserError("cancelled property can't be sold.")
            else: record.state = 'sold'

    # # now to check that the expected price must be strictly positive
    # @api.constrains('expected_price')
    # def _check_expected_price(self):
    #     for property in self:
    #         if property.expected_price <= 0:
    #             raise exceptions.ValidationError("expected price cannot be negative.")
    
    # # now to check that the property selling price is not negative
    # @api.constrains('selling_price')
    # def _check_selling_price(self):
    #     for property in self:
    #         if property.selling_price <= 0:
    #             raise exceptions.ValidationError("selling price cannot be negative.")

    # now to check that the selling price is not less than 90% of its expected price
    #    -1 : If the first value is less than the second value.
    #    0 : If the first value is equal to the second value.
    #    1 : If the first value is greater than the second value.	
    
    @api.constrains('expected_price', 'selling_price')
    def _selling_price(self):
        for record in self:
            if not float_is_zero(record.expected_price, precision_digits=2) and not float_is_zero(record.selling_price, precision_digits=2):
                if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
                    raise exceptions.ValidationError("Selling price cannot be lower than 90 percent of the expected price!")

   