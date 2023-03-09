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
   _order="id desc"
   _inherit="estate.inheritance"
   _inherit = ['mail.thread', 'mail.activity.mixin']
   
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
   garden_area = fields.Integer(string="Garden Area(sqm)", compute="_compute_garden" ,readonly=False)
   garden_orientation = fields.Selection(
      selection =[('N','North'),('E' , 'East'),('S','South'),('W','West')],
      help = 'Type is used to seprate directions' , 
      compute="_compute_garden", readonly=False,
      string="Garden Orientation",
      tracking =True,
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
      string="Status" ,default = "new",copy = False, required =True, 
      tracking =True,
   )
   
   property_type_id=fields.Many2one("estate.property.type" , string="Property Type")
   user_id = fields.Many2one("res.users", string="Salesperson",default=lambda self: self.env.user)
   buyer = fields.Many2one("res.partner", string="Buyer", index=True , copy=False)    # copy=false it means when we duplicate a record it is not copied
   tag_ids= fields.Many2many("estate.property.tag" ,relation="estate_property_tag_rel")
   offer_ids = fields.One2many("estate.property.offer","property_id")
   total_area=fields.Float(compute="_compute_total_area" , tracking = True)
   best_price=fields.Float(compute="_compute_best_price")
   seq_name = fields.Char(string='Property Reference', required=True,readonly=True, default=lambda self: ('New'))
   favorite = fields.Boolean()
   kanban_state = fields.Selection([
      ('normal','Grey'),
      ('done','Green'),
      ('blocked','Red')], string='Kanban State')
   color = fields.Integer(compute="_compute_color",default=4)
   image=fields.Image()

   @api.depends("state")
   def _compute_color(self):
      for record in self:
         if(record.state=="new"):
            record.color = 4
         elif(record.state=="offer_received"):
            record.color = 8
         elif(record.state=="offer_accepted"):
            record.color = 3
         elif(record.state=="sold"):
            record.color = 10
         else:
            record.color = 1


   @api.depends("garden_area","living_area")
   def _compute_total_area(self):
      for record in self:
         record.total_area=record.living_area + record.garden_area

   @api.depends("offer_ids")   
   def _compute_best_price(self):
      for record in self:
         if(record.offer_ids):
            if record.state == "new":
               record.state="offer_received"
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

   @api.constrains('selling_price')
   def _check_price_difference(self): 
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
   #           raise ValidationError("error")

   # CRUD operations

   @api.ondelete(at_uninstall=False)
   def unlink_except_available(self):
      for record in self:
         if record.state not in ['new','cancelled']:
            raise UserError("Only new and canceled properties can be deleted.")

   # method for ir sequence
   @api.model
   def create(self,vals):
      vals['seq_name'] = self.env['ir.sequence'].next_by_code('estate.property')
      return super(EstateProperty,self).create(vals)