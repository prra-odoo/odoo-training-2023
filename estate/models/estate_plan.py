# -*- coding: utf-8 -*-

from odoo import fields,models
from dateutil.relativedelta import relativedelta

class EstatePlan(models.Model):
    _name = "estate.property"
    _description = "This is Estate property model"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode', required=True)
    date_availability = fields.Date(string='Date', copy=False, default= lambda self: fields.datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(string='Expected_price', required=True)
    selling_price = fields.Float(string='Selling_price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living_area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden_area')
    garden_orientation = fields.Selection(
        string='Garden_orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    status = fields.Selection(
        string='Status',
        selection=[('new','New'),('offer_received','Offer Received')],
        default= 'new'
    )
    active = fields.Boolean(string='Active', default=True)
    