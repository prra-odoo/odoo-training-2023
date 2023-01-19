# -*- coding: utf-8 -*-

from odoo import api,fields, models,exceptions
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.tools import float_utils


class Real_estate(models.Model):
    _name="estate.property.model" # according to the naming conventions we do not add model in model's name
    _description="Real Estate Model"
    # _order = "id desc"

    name = fields.Char(required=True,default="New User")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=fields.date.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(default=0,readonly=False,copy=False)
    bedrooms = fields.Integer(default="2")
    active = fields.Boolean(default=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    state=fields.Selection(
        string='State',
        selection=[('new','New'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancled','Canceled')],
        required=True,
        copy=False,
        default='new'
    )
    garden = fields.Boolean()
    garden_area = fields.Integer(compute="_compute_garden_area",readonly = False)
    garden_orientation = fields.Selection(string='orientation',
    selection=[('north','North'),('east','East'),('west','West'),('south','South')],default='east')

    # use of relational fields
    type_id=fields.Many2one("estate.property.type")
    buyer_id = fields.Many2one("res.partner",copy=False)
    salesperson_id = fields.Many2one("res.users",default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer","property_id",string="offer")
    total_area = fields.Float(compute="_compute_area")
    best_price = fields.Float(compute="_compute_best_price")
    

    # use of decorator
    @api.depends('living_area','garden_area')
    def _compute_area(self):
        
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):

        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'),default=0)


    @api.depends('garden')
    def _compute_garden_area(self):
            for record in self:
                if record.garden:
                    record.garden_area= 10
                    record.garden_orientation= 'north'
                else:
                    record.garden_area = 0
                    record.garden_orientation = ''


    def perform_cancel(self):
        for record in self:
            if record.state!='sold':
                record.state = 'cancled'
            else:
                raise exceptions.UserError("Sold properties cannot be canceled.")
        return True

    def perform_sold(self):
         for record in self:
            if record.state!='cancled':
                record.state = 'sold'
            else:
                raise exceptions.UserError("Canceled properties cannot be sold.")

         return True

    # use of constraints

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The Expected Price Should Be Positive'),
         ('check_selling_price', 'CHECK(selling_price > 0)',
         'The Selling Price Should Be Positive'),
        
    ]

    @api.constrains('expected_price','selling_price')
    def _check_sellingprice(self):
        
        for record in self:
            

            if  (float_utils.float_compare(record.selling_price, 0.9 * record.expected_price,precision_digits=2) == -1 and  not float_utils.float_is_zero(record.expected_price,precision_digits=2)) :
                 raise exceptions.ValidationError("The Offer price cannot be lower than 90% of the expected price.")


    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_canceled(self):
        for record in self:
            if record.state not in ['new','cancled']:
                raise exceptions.UserError('You can delete only new and cancled properties')

    @api.model
    def create(self,vals):
        print("Create function called")
        # t=self.env['estate.property.model'].browse(vals['type_id'])
        # t.state = 'offer_recieved'
        return super(Real_estate,self).create(vals)
            
            
            
            
     
        

        
            
        
            

