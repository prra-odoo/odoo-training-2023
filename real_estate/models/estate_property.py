# -*- coding: utf-8 -*-

from odoo import models,fields

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "The Real Estate Advertisement Module"

    name = fields.Char('Name', required=True, copy=True)
    description = fields.Text('Description')
    postcode = fields.Integer('Postcode')
    date_availability = fields.Date('Date Availability', default=lambda self: fields.Datetime.now())
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Garden Orientation',
        selection=[('east', 'East'), ('west', 'West'), ('north', 'North'), ('south', 'South')]
        )
    state = fields.Selection(selection=[('new', 'New'), ('in progress', 'In Progress'), ('cancel', 'Cancel')],
                                        default='new'
        )
    last_seen = fields.Char('Last seen')
    active = fields.Boolean(default = True)
    property_type_id = fields.Many2one("estate.property.type", string='Property Type')
    buyer_id = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesman_id = fields.Many2one("res.users",string="Salesperson", default=lambda self: self.env.user )
    tag_ids=fields.Many2many("estate.property.tag", string='property Tags')
    offer_ids=fields.One2many("estate.property.offer","property_id")