# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property Model"

    name = fields.Char(required=True)
    description = fields.Text()
    user_id = fields.Many2one('res.users', string='Salesperson',
                              index=True, default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Buyer', index=True)
    property_type_id = fields.Many2one(
        'estate.property.type', required=True, index=True)
    property_tag_id = fields.Many2many(
        'estate.property.tag', relation='tag_connection', required=True)
    postcode = fields.Char(required=True)
    date_availability = fields.Date(
        default=lambda self: fields.Datetime.now() + relativedelta(months=3), copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute='_compute_garden',readonly=False,store=True)
    total_area = fields.Integer(
        compute="_compute_total_area", string="Total Area")
    best_offer = fields.Float(
        compute="_compute_best_offer", string="Best Offer")
    log_access = True
    garden_orientation = fields.Selection(
        string='Garden Orientattion',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')], compute='_compute_garden',readonly=False,store=True
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer', 'Offer'), ('recevied', 'Recevied'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        required=True,
        copy=False,
        default='new',
    )
    offers_id = fields.One2many('estate.property.offer', 'property_id')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('offers_id')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.mapped(
                'offers_id.price'), default='0')

    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_orientation = 'north'
                record.garden_area = 10
            else:
                record.garden_orientation = None
                record.garden_area = 0

    def action_sold(self):
        for record in self:
            if record.state == "sold":
                raise UserError("This property alredy sold")
            elif record.state == "cancelled":
                raise UserError("This property can not be sold because it was cancelled")
            else:
                record.state = "sold"
        return True

    def action_cancel(self):
        for record in self:
            if record.state == "cancelled":
                raise UserError("This property alredy cancelled")
            elif record.state == "sold":
                raise UserError("This property can not be cancel because it was sold")
            else:
                record.state = "cancelled"
        return True

    

    
