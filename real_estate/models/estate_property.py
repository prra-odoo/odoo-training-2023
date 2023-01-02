# -*- coding: utf-8 -*-
from odoo import models,fields

class estate_property(models.Model):
    _name = 'estate.property'
    _description = "Real Estate Module"

    name = fields.Char('Property Name',required=True)
    description = fields.Char('Description')
    postcode = fields.Char('PostCode')
    date_availability = fields.Datetime('Date',readonly=True)
    expected_price = fields.Float('Expected Price',readonly=True,required=True)
    selling_price = fields.Float('Selling Price',readonly=True)
    bedrooms = fields.Integer('#Bedrooms')
    living_area = fields.Integer('#living area')
    facades = fields.Integer('#Facades')
    garage = fields.Boolean('Active',default=True)
    garden = fields.Boolean('Active',default=True)
    garden_area = fields.Integer('#Garden_area')
    garden_orientation = fields.Selection(
            string='Type',
            selection=[('North','North'),('South','South'),('East','East'),('West','West')],
            help="This type is saparate north ,south,east and wast")

