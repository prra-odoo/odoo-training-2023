# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from dateutil.relativedelta import relativedelta
from odoo.tools.date_utils import add
from odoo.exceptions import UserError, ValidationError

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property module "

    name = fields.Char(required=True)
    id = fields.Integer()
    postcode = fields.Char()
    description = fields.Text(copy=False)
    # date_availability = fields.Date('Date Avilability',default=lambda self: fields.datetime.today()+relativedelta(months=3))
    date_availability = fields.Date('Date Avilability',default=lambda self:add(fields.datetime.today(),months=3))
    expected_price = fields.Float("Expected Price")
    selling_price = fields.Float("Selling Price",default=2000000)
    bedrooms = fields.Integer(default=3)
    living_area = fields.Integer("Lving Area")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer("Garden Area")
    other_info=fields.Text('Other Info')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    state = fields.Selection( 
        string='State', 
    selection = [('new', 'New'),('in_progress', 'In Progress'),('sold', 'Sold'),('cancel', 'Cancelled')])
    property_type_id=fields.Many2one("estate.property.type",string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesman_id = fields.Many2one('res.users', string='Salesman')
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids=fields.One2many('estate.property.offer','property_id',string="Offers")
    total_area=fields.Integer("Total Area",compute='_compute_total_area')
    best_price=fields.Float("Best Offer",compute="_compute_best_price", default =0)


    @api.depends('garden_area','living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.garden_area+record.living_area 
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price=max(record.offer_ids.mapped('price'))

    def sold_button(self):
        for record in self:
            if record.state =="cancel":
                raise UserError(("Cancelled property cannot be sold!"))
            else:
                record.state ="sold"
        return True

    def cancelled_button(self):
        for record in self:
            if record.state=="sold":
                raise UserError(("Sold property cannot be Cancelled!"))
            else:
                record.state=="cancel"
        return True


    _sql_constraints = [('check_expected_price','CHECK(expected_price>0)','Expected Price must be positive.'),
    ('check_selling_price','CHECK(selling_price>0)','Selling Price must be positive.'),
    ('check_living_area','CHECK(living_area>0)','Living Area must be positive.'),
    

    ]




