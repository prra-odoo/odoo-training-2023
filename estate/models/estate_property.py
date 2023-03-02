from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property detailed field"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"    # _order use to change display record in the list view by default on id and asc order
     # contraints can not be apply on table and not change contraints
    _sql_constraints = [
        (
            'check_prices_possitive',
            'CHECK(expected_price > 0.0 AND selling_price >= 0.0)',
            "Expected price and Selling price are not be negative.\n Expected price also not possible Zero(0)."
        )
    ]
    

    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char(default="0")
    # default=datetime.datetime.now().date()+datetime.timedelta(days=90)
    date_availability = fields.Date(readonly=True,default=lambda self:(fields.Datetime.now().date()+relativedelta(months=+3)))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Float()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Float()
    #selection is use to create dropdown and radio
    garden_orientation = fields.Selection(
        string = "Direction",
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help  = "Select Direction",
        compute="_compute_garden",
        readonly=False
        )
         
    active = fields.Boolean("Active",default=True)
    state = fields.Selection(
        string = "Status",
        selection = [('new','New'),('received','Offer Received'),('accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        help  = "Status",
        default = "new",
        copy=False,
        tracking = True
        )
    
    property_type_id = fields.Many2one('estate.property.type',string="Property Type")
    property_tag_ids = fields.Many2many('estate.property.tag', string="Property Tag", relation="tag_table")
    offer_ids = fields.One2many('estate.property.offer',"property_id",string="Offers")
    
    buyer_id = fields.Many2one('res.partner',copy=False, readonly=True)
    salesmans_id = fields.Many2one('res.users', default=lambda self:self.env.user)
    user_id = fields.Many2one('res.users',string="User")

    total_area = fields.Float(string='Total Area', readonly=True, compute = "_compute_total_area")
    best_price = fields.Float(compute = "_compute_best_offer" ,string="Best Price", readonly=True)
    #ir.sequence
    property_seq = fields.Char(string='Property ID',required=True,readonly=True,
                                default=lambda self: ('New'))

    @api.model
    def create(self,vals):
        vals['property_seq'] = self.env['ir.sequence'].next_by_code('estate.property')
        print(vals['property_seq'])
        return super(EstateProperty,self).create(vals)

   
    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    

    #api.depends use to set dependancy on function. parameters field change value or on save action  then call this function
    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for record in self:
            if(record.offer_ids):
                if(record.state == "new"):
                    record.state = 'received'
                record.best_price = max(record.offer_ids.mapped('price'))
            else: 
                record.best_price = 0.0
                if(record.state == 'received'):
                    if(not record.offer_ids):
                        record.state = 'new'


    
    
    # api.onchange use to set dependancy on function when parameter field change data it call automatically
    @api.depends('garden')
    def _compute_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north' 
        else:
            self.garden_area = 0
            self.garden_orientation = '' 
    
    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for record in self:
            # if(record.selling_price < (record.expected_price*0.9)):
            #     raise ValidationError('Selling price is more less than experted price ')
            if(not((float_is_zero(value=record.selling_price, precision_digits=2)))
               and
               not (float_is_zero(value=record.expected_price, precision_digits=2))):
                if(float_compare(value1=record.selling_price, value2=(record.expected_price* 0.9), precision_digits=2) == -1):
                
                    raise ValidationError('Selling price is more less than experted price ')
    
    
    
    #sold button action
    def action_do_sold(self):
        for record in self:
            if( record.state == 'canceled'):
                raise UserError(("Cancel Property (%s) can not be Sold.")% record.name)
            else:
                record.state = "sold"
        return True
    
    #cancel button action
    def action_do_cancel(self):
        for record in self:
            record.state = "canceled"
        return True
    
    @api.ondelete(at_uninstall = False)
    def _unlink_except_posted_or_approved(self):
        if (self.state not in ['new','canceled']):
            raise UserError("New or Canceled Property can not be deleted")
        # return()

