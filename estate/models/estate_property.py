# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate_property Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date(
        default=lambda self: fields.Date.today() + relativedelta(months=3), copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute='_compute_garden_fields',store=True, readonly=False)
    garden_orientation = fields.Selection(
        string='Garden Orientattion',compute='_compute_garden_fields',store=True, readonly=False,
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
    )
    total_area = fields.Integer(compute = "_compute_total_area")
    best_price = fields.Float(compute = "_compute_best_price")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer_recieved', 'Offer_Recieved'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        required=True,
        copy=False,
        default='new',
    )
    user_id = fields.Many2one(comodel_name='res.users', string='Salesperson',
                              index=True, default=lambda self: self.env.user)
    buyer_id=fields.Many2one(comodel_name='res.partner',string='Buyer',index=True)
    property_type_id = fields.Many2one(comodel_name='estate.property.type',required=True,index=True)
    tag_ids = fields.Many2many(comodel_name='estate.property.tags',relation='tag_table',required=True)
    offer_ids=fields.One2many(comodel_name='estate.property.offers',inverse_name='property_id') 

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                record.best_price = max(record.offer_ids.mapped("price"))
                print(record)
            else:
                record.best_price = 0.0

    # @api.depends('offer_ids')
    # def _compute_best_price(self):
    #     for record in self:
    #         if(record.offer_ids):
    #             record.best_price = max(offer.price for offer in record.offer_ids)
    #         else:
    #             record.best_price = 0.0

    @api.depends("garden")
    def _compute_garden_fields(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False 

    def action_sold(self):
        for record in self:
            if record.state != "cancelled":
                record.state = "sold"
            else:
                raise UserError("This property can not be sold because it is cancelled")
        return True
    
    def action_cancel(self):
        for record in self:
            if record.state != "sold":
                record.state = "cancelled"
            else:
                raise UserError("This property can not be cancelled because it is sold")
        return True
            