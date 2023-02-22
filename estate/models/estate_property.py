# -*- coding: utf-8 -*-
from odoo import *
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_utils

class EstateProperty(models.Model):
    _name="estate.property"
    _inherit = ['mail.thread']
    _description="Estate Property Description"
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price>0)','The Expected Price must be strictly positive'),
        ('check_selling_price','CHECK(selling_price>=0)','The Selling Price must be positive')
    ]
    _order = "id desc"
    
    
    name = fields.Char(required=True,string="Title")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=lambda self: fields.Date.today()+relativedelta(months=3),string="Available From")
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(default=True)
    garden_area = fields.Integer(string="Garden Area (sqm)",compute="_compute_garden",inverse="_inverse_garden",store=True)
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[('north',"North"),('south',"South"),('east',"East"),('west',"West")],
        compute="_compute_garden",
        inverse="_inverse_garden",
        store=True,
    )
    active = fields.Boolean(default=True,required=True)
    state = fields.Selection(
        string="State",
        required=True,
        selection=[('new',"New"),('offer_received',"Offer Received"),('offer_accepted',"Offer Accepted"),('sold',"Sold"),('cancelled',"Cancelled")],
        default='new'
    )
    property_type_id = fields.Many2one("estate.property.type",string="Property Type",required=True)
    buyer_id = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesperson_id = fields.Many2one("res.users",string="Salesman",default= lambda self : self.env.user)
    tag_ids = fields.Many2many("estate.property.tag",string="Tags",relation="property_tags_rel",column1="property_id",column2="tag_id")
    offer_ids = fields.One2many("estate.property.offer","property_id",string="Offers")
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer = fields.Float(compute="_compute_best_offer")
    color = fields.Integer(compute="_compute_color",default=4)

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

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.living_area+record.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            if(record.offer_ids):
                if(record.state=="new"):
                    record.state="offer_received"
                record.best_offer=max(record.offer_ids.mapped("price"))
            else:
                if(record.state=="offer_received"):
                    record.state="new"
                record.best_offer=0.0

    @api.depends("garden")
    def _compute_garden(self):
        for record in self:
            if(record.garden==False):
                record.garden_area = 0
                record.garden_orientation=""
            else:
                record.garden_area = 10
                record.garden_orientation = "north"
    
    def _inverse_garden(self):
        pass

    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for record in self:
            if((not float_utils.float_is_zero(record.selling_price,2)) and ((float_utils.float_compare(record.expected_price-record.selling_price,record.expected_price*0.1,0))==1)):
                raise ValidationError("The Selling Price must be at least 90% of the expected price")

    def action_sold(self):
        for record in self:
            if(record.state!="cancelled"):
                record.state = "sold"
            else:
                raise UserError("Cancelled Property can not be Sold.")
            return True

    def action_cancel(self):
        for record in self:
            if(record.state!="sold"):
                record.state = "cancelled"
            else:
                raise UserError("Sold Property can not be Cancelled.")
            return True