# -*- coding: utf-8 -*-

from odoo import models,fields

class realEstate(models.Model):
    _name = "real.estate"
    _description = "The Real Estate Advertisement Module"

    name = fields.Char('Name', required=True, readonly=True, copy=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type',
        selection=[('lead', 'Lead'), ('opportunity', 'Opportunity')],
        help="Type is used to separate Leads and Opportunities"
        )




