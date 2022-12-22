# -*- coding: utf-8 -*-

from odoo import models,fields

class realestate(models.Model):
    _name = "real.estate"
    _description = "The Real Estate Advertisement Module"

    name = fields.Char('Name', required=True, readonly=True, copy=True)
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
    garden_orientation = fields.Selection(string='Type',
        selection=[('lead', 'Lead'), ('opportunity', 'Opportunity')]
        )




