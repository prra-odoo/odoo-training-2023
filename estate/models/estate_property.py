from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import UserError,ValidationError,AccessError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _order="sequence,id desc"
    _inherit = 'inherit.fields'
    _inherit = ['mail.thread', 'mail.activity.mixin']
  

    name=fields.Char(required=True)
    description=fields.Char()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False, default= lambda self:(fields.Datetime.now().date()+relativedelta(months=+3)))

    sequence=fields.Integer('Sequence',default=1,help="Used to order stages")


    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer(compute="_compute_garden",readonly=False,store=True)
    garden_orientation=fields.Selection(
        
        selection=[('E','East'),('W','West'),('N','North'),('S','South')],
        string="Garden Orientation",
        compute="_compute_garden",
        readonly=False,
        

        store=True,

        
    )

  
    state=fields.Selection(
        selection=[
            ('new','New'),
            ('offer_received','Offer Received'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled')
    
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
        compute="_compute_state",
        store=True,
        tracking=True

    )



    active=fields.Boolean("Active",default=True)

    total_area=fields.Integer(string="Total Area",compute="_compute_area")
    best_offer=fields.Float(string="Best Price",compute="_compute_best_offer")

    property_type_id=fields.Many2one('estate.property.type',string="Property Type")
    buyer_id=fields.Many2one('res.partner', string='Buyer',copy=False)

    salesperson_id=fields.Many2one('res.users',string="Salesman",default=lambda self:self.env.user)
    tag_ids=fields.Many2many('estate.property.tag',relation="tag_property")
    offer_ids=fields.One2many('estate.property.offer','property_id',string="Offer")
    property_image=fields.Binary(string="Image here")
    color_kanban=fields.Integer(default=1)



    @api.constrains('selling_price')
    def _check_selling_price(self):
      for record in self:
        if record.selling_price < record.expected_price*0.90:
            raise ValidationError("The selling price less than 90% of the expected price could not be accepted")


    _sql_constraints=[
        ('check_expected_price','CHECK (expected_price>=0)','Expected peice must be positive.'),
         ('check_selling_price','CHECK (selling_price>=0)','Selling price must be positive.')
    ]

    @api.depends('living_area','garden_area')
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
              

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            if record.offer_ids:
                record.best_offer=max(record.offer_ids.mapped('price'))            
            else:
                record.best_offer=0
                
    @api.depends('offer_ids','offer_ids.status')
    def _compute_state(self):
       if self.offer_ids:
        self.state="offer_received"
 


                 


    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_area=10
                record.garden_orientation="N"
            else:
                record.garden_area=False
                record.garden_orientation=False


    def action_sold(self):
         if self.state == "cancelled":
            raise UserError("The cancelled properties cannot be sold")
         else:
            self.state="sold"

    def action_cancel(self):
         if self.state == "sold":
            raise UserError("Sold Properties cannot be cancelled")
         else:
            self.state="cancelled"
       


    @api.ondelete(at_uninstall=False)
    def _unlink_except_offer_received_accepted_sold(self):
        if self.state not in ['new','cancelled']:
            raise AccessError("Only new and cancelled properties can be deleted")

           
    # @api.ondelete(at_uninstall=False)
    # def _unlink_except_contains_journal_items(self):
    #     if self.env['account.move.line'].search([('account_id', 'in', self.ids)], limit=1):
    #         raise UserError(_('You cannot perform this action on an account that contains journal items.'))





class InheritedProperty(models.Model):
        _inherit = "estate.property"

        price=fields.Integer()
        date=fields.Date()
