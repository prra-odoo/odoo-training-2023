from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError
from odoo.tools.float_utils import float_is_zero,float_compare

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Model"
    _sql_constraints = [
        ('expected_price', 'CHECK(expected_price > 0)',
         'The expected price should be strictly positive only.'),
        ('selling_price', 'CHECK(selling_price > 0)',
         'The selling price price should be strictly positive only.'),
    ]
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin','base.property']

    id = fields.Integer()
    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    postcode = fields.Char()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    date_availability = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default='2')
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()   
    garden_area = fields.Integer(compute='_compute_garden_values',store=True)
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Select your direction!",compute='_compute_garden_values')
    active = fields.Boolean(default=True,required=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer recieved', 'Offer Recieved'), 
        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required="true",copy=False)

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    # test = fields.Integer(related="property_type_id.offer_count")
    salesman_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer",copy=False, readonly=True)
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags", relation="many2many_mash_tags_rel")
    offer_ids = fields.One2many("estate.property.offer", "property_id")

    total_area = fields.Integer(compute="_total_area")
    @api.depends('living_area','garden_area')
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_offer = fields.Float(compute='_best_offer')
    @api.depends('offer_ids')
    def _best_offer(self):
        for record in self:
            if record.offer_ids:
                if(record.state == "new"):
                    record.state = "offer recieved"
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer =  0.0
                if(record.state == "offer recieved"):
                    if(not record.offer_ids):
                        record.state = "new"

    @api.depends('garden')
    def _compute_garden_values(self):
        for record in self:
            if (record.garden==True):
                record.garden_area = 10.0
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0.0
                record.garden_orientation = False
    def _inverse_garden(self):
        pass
    
    def action_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError('A canceled property cannot be sold')
            else:
                record.state = 'sold'

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('A sold property cannot be cancelled')
            else:
                record.state = 'cancelled'

    # now to check that the selling price is not less than 90% of its expected price
    #    -1 : If the first value is less than the second value.
    #    0 : If the first value is equal to the second value.
    #    1 : If the first value is greater than the second value.

    @api.constrains('expected_price', 'selling_price')
    def _selling_price(self):
        for record in self:

            if not float_is_zero(record.expected_price, precision_digits=2) and not float_is_zero(record.selling_price, precision_digits=2):
                if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
                    raise ValidationError("Selling price cannot be lower than 90 percent of the expected price!")
                


# class ResUsers(models.Model):
#     _inherit = "res.users"

#     property_ids = fields.One2many("estate.property", "salesman_id", domain="[('state', 'in', ['new','offer recieved'])]")
    


    

    
    

