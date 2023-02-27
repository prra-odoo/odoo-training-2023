from odoo import api,fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo import *
from odoo.tools.float_utils import *
# from odoo import EstatePropertyOffer
class EstatePlan(models.Model):
    _name = "estate.property"
    _description = "estate property"
    _order = "id desc"
    _inherit="estate.inheritance"

   
    # name = fields.Char(required=True, string="Title")
    property_type_id = fields.Many2one("estate.property.types",string = "Property Types")
    property_tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")
    active = fields.Boolean(default = True)
    description = fields.Text()
    # state = fields.Text()
    # postcode = fields.Char()
    # dateavailability = fields.Date(copy=False, default=lambda self: fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    # living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    # garden_area = fields.Integer()
    garden_direction = fields.Selection(
        string = "Garden Orientaiton",
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help = "Choose the direction",
        default='north'
    )
    state = fields.Selection(
        string = "state",
        selection = [('new','New'),('offered received','Offered Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled'),],
        default='new',
        help = "Choose the state",
        required = True
    )
    buyer = fields.Many2one("res.partner", string="Buyer")
    salesperson = fields.Many2one("res.users",string = "Salesperson", default=lambda self: self.env.user)
    price = fields.Float(string="Price")
    status = fields.Selection(copy=False,selection=[('accepted','Accepted'),('refused','Refused')])
    offer_ids = fields.One2many("estate.property.offer","property_id",required=True)
    totalarea = fields.Float(compute="_total_area")

    living_area = fields.Float()
    garden_area = fields.Float(compute="_compute_garden_area",inverse="_inverse_garden_area")
        
    @api.depends("living_area","garden_area")
    def _total_area(self):
        for area in self:
            area.totalarea = area.living_area + area.garden_area

    best_price=fields.Integer(compute="_max_price",readonly=True)
    
    @api.depends("offer_ids")
    def _max_price(self):
        for highest in (self):
            if (highest.offer_ids):
                if highest.state == "new":
                    highest.state = "offered received"
                highest.best_price=max(highest.offer_ids.mapped('price'))
            else:
                highest.best_price = 0

    # @api.onchange("garden")
    # def _onchange_garden(self):
    #     if self.garden:
    #         self.garden_area = 10
    #         self.garden_direction = "north"

    #     else:
    #         self.garden_area = 0

    @api.depends("garden")
    def _compute_garden_area(self):
        if self.garden:
            self.garden_area=10
            self.garden_direction="north"
        else:
            self.garden_area=0
    
    @api.depends("garden_area")
    def _inverse_garden_area(self):
        if self.garden_area!=0:
            self.garden=True
        else:
            self.garden = False

    def action_sold(self):
        for record in self:
            if record.state != "canceled":
                record.state = "sold"
            else:
                raise UserError("Property Cancelled Cannot Be Sold")
            return True

    def action_canceled(self):
        for record in self:
            if record.state != "sold":
                record.state = "canceled"
            else:
                raise UserError("Property Sold Cannot Be Cancelled")   
            return True 
    
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            sp = (90 * record.expected_price) / 100
            if(not float_is_zero(record.selling_price, precision_rounding=0.01)):
                if (float_compare(sp,record.selling_price, precision_rounding=0.01) >= 0):
                    raise ValidationError("The selling price must be at least 90%")
            
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)','The Expected value should be positive.'),
        ('check_selling_price', "CHECK(selling_price >=0)","Selling Price must be positive"),
    ]