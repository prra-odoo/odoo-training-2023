# -*- coding:utf:8 -*-

from odoo import models, fields, api



class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Advertisement module"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(
        string='Date Available', default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(string='Price', required=True)
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    garden_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('south', 'South'), ('west', 'West'),
                   ('north', 'North'), ('east', 'East')]
    )
    state = fields.Selection(
        selection=[('new', 'New'), ('confirm', 'Confirm'),
                   ('cancel', 'Cancel')], default="new"
    )
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    salesperson_id = fields.Many2one(
        'res.users', string="Sales Person", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many("estate.property.offer","property_id")

    total_area = fields.Integer(compute="_compute_total_area")
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area 

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'),default=0)