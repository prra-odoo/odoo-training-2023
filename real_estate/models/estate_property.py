from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_is_zero,float_compare

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "CRM Recurring revenue plans"
    _order = "id desc"

    name = fields.Char(required=True)
    description=fields.Char()   
    postcode = fields.Char(default="0")
    date_availability = fields.Date(readonly=True, default=lambda self:(fields.Datetime.now().date()+relativedelta(months=+3)))
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    total_area=fields.Float(compute="_total_area",readonly=True)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(store=True)
  
    
    garden_area = fields.Integer(compute="_compute_area",store=True,readonly=False)
    best_price = fields.Float(compute="_compute_discount")
    garden_orientation = fields.Selection(
        string='Type',compute="_compute_area",readonly=False,store=True,
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help="Type is used to separate Directions"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection = [('new','New'),('off_re','Offer Received'),('off_ac','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        required=True,default="new",copy=False
    )

    property_type_id=fields.Many2one('estate.property.type',string="Property Type")
    property_tag_ids=fields.Many2many('estate.property.tag',relation='property_tag_rel',string="Property Tag")
    offer_ids=fields.One2many('estate.property.offer','property_id',string="Offer")


    
    buyers_id=fields.Many2one('res.partner',copy=False)
    salesmen_id=fields.Many2one('res.users',default=lambda self:self.env.user)

    #sum of the living_area and the garden_area.
    @api.depends("living_area","garden_area")
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    #Compute the best offer.
    #highest of the offers price.
    @api.depends("offer_ids")
    def _compute_discount(self):
        for record in self:
            if(record.offer_ids): 
                if(record.state=='new'):
                    record.state='off_re'
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price=0.0 


    #Set values for garden area and orientation.
    @api.depends("garden")
    def _compute_area(self):
        for record in self:
            if record.garden:
                record.garden_area=10
                record.garden_orientation='north'
            else:
                record.garden_area=False
                record.garden_orientation=False

    #canceled property cannot be set as sold, and a sold property cannot be canceled.
    def action_sold(self):
        for record in self:
            if record.state == "canceled":
                raise UserError("Cancelled properties not sold.")
            else:
                record.state="sold"
            
            
    def action_cancle(self):
        for record in self:
            if record.state == "sold":
                 raise UserError("Sold properties not be cancelled.")
            else:
                record.state="canceled"
           

    #expected price must be strictly positive,selling price must be positive
    _sql_constraints = [
        ('check_expected','CHECK(expected_price >= 0)','Expected Price Must Be In Possitive Value.'),
         ('check_selling','CHECK (selling_price>=0)','selling price must be possitive')
    ]
    
    # @api.constrains('selling_price','expected_price')
    # def _check_selling_expected(self):
    #     for record in self:
    #         if record.selling_price < record.expected_price*0.9:
    #             raise ValidationError("Selling Price Is Greter Then Expected Price")

    @api.constrains('expected_price','selling_price')
    def _check_selling_expected(self):
      for record in self:
        if not float_is_zero(record.expected_price, precision_digits=2) and not float_is_zero(record.selling_price, precision_digits=2):
          if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
            raise exceptions.ValidationError("Selling price cannot be lower than 90 percent of the expected price!")

   
  

    