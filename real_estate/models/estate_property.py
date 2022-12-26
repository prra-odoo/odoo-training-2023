# -*- coding: utf-8 -*-

from odoo import models,fields

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "The Real Estate Advertisement Module"

    name = fields.Char('Name', required=True, copy=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
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




