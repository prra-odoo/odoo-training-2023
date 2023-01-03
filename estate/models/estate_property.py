# -*- coding: utf-8 -*-

from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.tools.date_utils import add

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
    selling_price = fields.Float("Selling Price",readonly=True,default=2000000)
    bedrooms = fields.Integer(default=3)
    living_area = fields.Integer("Lving Area")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer("Garden Area")
    other_info=fields.Text('Other Info')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )

    state = fields.Selection( 
        string='State', 
    selection = [('new', 'New'),('in_progress', 'In Progress'),('cancel', 'Cancelled'),('sold', 'Sold')])

    property_type_id=fields.Many2one("estate.property.type",string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesman_id = fields.Many2one('res.users', string='Salesman')
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids=fields.One2many('estate.property.offer','property_id',string="Offers")
    total_area=fields.Integer("Total Area",compute='_compute_total_area')
    @api.depends('garden_area','living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.garden_area+record.living_area 


    best_price=fields.Float("Best Offer",compute="_compute_best_price", default =0)
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price=max(record.offer_ids.mapped('price'))

    def sold(self):
        for record in self:
            record.state="sold"
        if record.state =="cancel":
            raise ValueError("Sold property cannot be cancleled")
        else:
            record.state =="sold"

        return True

    def cancle(self):
        for record in self:
            record.state="cancel"
        return True




