from odoo import models, fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError ,ValidationError
from odoo.tools import float_compare , float_is_zero



class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a real estate property model"  
    _sql_constraints=[
       ("check_expected_price","CHECK(expected_price > 0)","The expected price must be strictly positive"),
                  ("check_selling_price","CHECK(selling_price >= 0)","The offer price must be strictly positive")
     ]
    
   

    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string='Availabel From', default=lambda self: fields.Date.today()+relativedelta(months=+3), copy=False)
    expected_price = fields.Float("Expected Price" ,required=True)
    selling_price = fields.Float(string='Selling Price',readonly=True , copy=False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer(string="Garden Area(sqm)", compute="_compute_garden")
    garden_orientation = fields.Selection(
        selection =[('N','North'),('E' , 'East'),('S','South'),('W','West')],
        help = 'Type is used to seprate directions' , 
        compute="_compute_garden"
    )
    active = fields.Boolean("Active", default = True)
    state = fields.Selection(
        selection=[
        ("new", "New"),
        ('offer_received','Offer Received'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')
        ],
        string="State" ,default = "new",copy = False, required =True, 
    )
    property_type_id=fields.Many2one("estate.property.type" , string="Property Type")
    salesperson = fields.Many2one("res.users", string="Salesperson",default=lambda self: self.env.user)
    buyer = fields.Many2one("res.partner", string="Buyer", index=True , copy=False)    # copy=false it means when we duplicate a record it is not copied
    tag_ids= fields.Many2many("estate.property.tag" , relation="estate_property_tag_rel")
    offer_ids = fields.One2many("estate.property.offer","property_id")
    total_area=fields.Float(compute="_compute_total_area")
    best_price=fields.Float(compute="_compute_best_price")
   
    
    
    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.living_area + record.garden_area
   
    @api.depends("offer_ids")   
    def _compute_best_price(self):
     for record in self:
        if(record.offer_ids):
            record.best_price=max(record.offer_ids.mapped("price"))
        else:
            record.best_price=0.0    

    @api.depends("garden")
    def _compute_garden(self):
       for record in self:
        if record.garden:
           record.garden_area=10
           record.garden_orientation="N"
        else:
           record.garden_area=0
           record.garden_orientation=""

   
    def action_set_sold(self):
     for record in self:
        if record.state=="canceled":
          raise UserError("canceled properties cannot be sold.") 
        else:
           record.state="sold"
        

    def action_set_cancel(self):
       for record in self:
          if record.state=="sold":
             raise UserError("sold property cannot be canceled.")
          else:
             record.state="canceled"

    @api.constrains('selling_price','expected_price')
    def check_price_difference(self): 
      for record in self:
         if (
            not float_is_zero(record.selling_price, precision_rounding=2)
            and float_compare(record.selling_price,record.expected_price*0.9 , precision_digits=2)==-1
           ):
            raise ValidationError("The selling price must be at least 90 percent of the expected price")

   #  @api.constrains("selling_price","expected_price")
   #  def check_price_difference(self):
   #     for record in self:
   #        if record.selling_price < record.expected_price*0.9:
   #           raise ValidationError("eroor")





