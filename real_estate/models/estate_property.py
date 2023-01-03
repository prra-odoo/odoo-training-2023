# -*- coding: utf-8 -*-

from odoo import api,models,fields
from datetime import date
from odoo.exceptions import UserError

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "The Real Estate Advertisement Module"

    name = fields.Char(string='Name', required=True, copy=True)
    description = fields.Text(string='Description')
    postcode = fields.Integer(string='Postcode')
    date_availability = fields.Date(string='Date Availability', default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden=fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation',
        selection=[('east', 'East'), ('west', 'West'), ('north', 'North'), ('south', 'South')]
        )
    state = fields.Selection(selection=[('new', 'New'), ('in progress', 'In Progress'), ('cancel', 'Cancel')],
                                        default='new'
        )
    last_seen = fields.Char(string='Last seen')
    active = fields.Boolean(default = True)
    property_type_id = fields.Many2one("estate.property.type", string='Property Type')
    buyer_id = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesman_id = fields.Many2one("res.users",string="Salesperson", default=lambda self: self.env.user )
    tag_ids=fields.Many2many("estate.property.tag", string='property Tags')
    offer_ids=fields.One2many("estate.property.offer","property_id")
    total_area=fields.Float(string="Total Area", compute="_compute_total", inverse="_inverse_total")
    best_offer=fields.Float(string="Best Offer",compute="_compute_best_offer")
    status=fields.Selection(string="Status", selection=[("sold", "Sold"), ("cancel", "Cancel")])


    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(self.offer_ids.mapped('price'), default=0)

    def sold_button(self):
        for record in self:
            if record.status=='cancel':
                raise UserError(('Cancelled property can not be sold.'))
            else:
                record.status = 'sold'

    def cancel_button(self):
        for record in self:
            if record.status=='sold':
                raise UserError(('Sold property can not be sold.'))
            else:
                record.status = 'cancel'

   
             