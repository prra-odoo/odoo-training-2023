# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate advertisement module"

    name = fields.Char('Name',required=True)
    description = fields.Text('Details',copy=False)
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date availability',default=lambda self:fields.Datetime.now(),readonly=True)
    expected_price = fields.Float('Expected price',required=True)
    selling_price = fields.Float('Selling price',readonly=True)
    bedrooms = fields.Integer('Bedroom',default='2')
    living_area = fields.Integer('Living area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),('confirm', 'Confirmed'), ('cancelled', 'Cancelled')],
        default='new',
    )
