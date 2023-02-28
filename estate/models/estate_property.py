from odoo import api, models,fields,_
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero
from odoo.tools.rendering_tools import relativedelta_proxy

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description='Real Estate Property'
        
    name = fields.Char(required=True)
    description = fields.Char()
    _order = "id desc"
    postcode = fields.Char()
    date_availability = fields.Date(copy = False,default = lambda self : fields.Date.today()+relativedelta_proxy(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy= False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute="_compute_garden",readonly = False, store = True)
    active = fields.Boolean(default = True)
    state = fields.Selection(
        string="State",
        default="new",
        selection=[('new','New'),('received','Offer Received'),('accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')],
      
    )
    
    garden_orientation = fields.Selection(
        string = "Type",
        selection = [('north','North'),('South','South'),('East','East'),('West','West'), ],
        help = "Choose the direction",
        compute = "_compute_garden",
        readonly = False,
        store = True
    )
    
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    buyer_id = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesperson_id = fields.Many2one("res.users",string="Salesperson",default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tags", string="Property Tags")
    offer_ids = fields.One2many("estate.property.offer","property_id", string="Offers")
    total_area = fields.Integer(compute="_compute_total")
    best_offer = fields.Float(compute = "_compute_bestoffer")
  
    
    #compute for total_area
    
    @api.depends("living_area","garden_area") #decorator
    
    def _compute_total(self):
        for record in self: 
            record.total_area = record.living_area + record.garden_area
    
    #compute for best_offer
            
    @api.depends("offer_ids.price")
    
    def _compute_bestoffer(self):
        for record in self:
            if record.offer_ids.mapped("price"):
                record.best_offer = max(record.offer_ids.mapped("price"))
            else:
                record.best_offer = 0
            
    #compute for garden_orientation and garden_area
    
    @api.depends("garden")
    
    def _compute_garden(self):
        for record in self:
                record.garden_orientation = "north" if record.garden == True else ""
                record.garden_area = 10 if record.garden == True else ""

    
    #sold button method
    
    def action_sold(self):
        for record in self:
            if record.state == "cancelled":
                raise UserError(_("cancelled property cannot be sold"))
            else:
                record.state = "sold"
            return True
        
    def action_cancel(self):
        for record in self:
            if record.state == "sold":
                raise UserError(_("sold property cannot be cancelled"))
            else:
                record.state = "cancelled"
            return True
                
    
    # SQL constraints
    
    _sql_constraints = [
        ("positive_expected_price","check(expected_price > 0)","The expected price must be strictly positive "),
        ("positive_selling_price","check(selling_price >= 0)","The selling price must be positive"),
        
    ]
    
    # python constrains
    
    @api.constrains("selling_price","expected_price")
    
    def _check_expected_price(self):
        for record in self:
            if (
                not float_is_zero(record.selling_price, precision_digits=2)
                and float_compare(record.selling_price, record.expected_price * 90.0 / 100.0, precision_digits=4) < 0
            ):
   
                raise ValidationError("The selling price must be atleast '90%' 0f expected price")
    
         