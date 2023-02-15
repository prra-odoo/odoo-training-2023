# -*- coding: utf-8 -*-
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string='Availability Date', default=lambda self: fields.Date.today()+relativedelta(months=+3), copy=False)
    expected_price = fields.Float(string='Expected Price',required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute='_compute_garden', string='Garden Area', readonly=False, store=True)
    garden_orientation = fields.Selection(
        selection = [('north', 'North'), ('east', 'East'),
                   ('south', 'South'), ('west', 'West')], compute='_compute_garden', readonly=False, store=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection = [('new','New'),
                     ('offer_received','Offer Received'),
                     ('offer_accepted','Offer Accepted'),
                     ('sold','Sold'),
                     ('canceled','Canceled')], default='new', copy=False)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many('estate.property.tag', relation='estate_property_tag_rel', string='Property Tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offer')
    total_area = fields.Integer(compute='_compute_total_area', string='Total Area')
    best_price = fields.Float(compute='_compute_best_price', string='Best Offer')
    status = fields.Char()

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
                if(record.offer_ids):
                     record.best_price = max(record.offer_ids.mapped("price"))
                else:
                     record.best_price = 0.0

    @api.depends('garden')
    def _compute_garden(self):
        if(self.garden):
            self.garden_area = 10
            self.garden_orientation = 'east'
        else:
            self.garden_area = None
            self.garden_orientation = None

    def action_sold(self):
        for record in self:
            if(record.status != "Canceled"):
                record.status = "Accepted"
            else:
                raise UserError("Canceled property can't be sold")
        return True
    
    def action_cancel(self):
        for record in self:
            if(record.status != "Accepted"):
                record.status = "Canceled"
            else:
                raise UserError("Sold property can't be canceled")
        return True
    