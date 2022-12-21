# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime, timedelta

class estateModel(models.Model):
    _name = "estate.model"
    _description = "Real Estate Module"

    name = fields.Char('Name',required=True,copy=False)
    description = fields.Text('Description',required=True)
    postcode = fields.Char(required=True)
    date_availability = fields.Datetime("Last Availability",default=lambda self:fields.Datetime.now())
    expected_price = fields.Float('Expected Price',readonly=True)
    selling_price = fields.Float(required=True,copy=False)
    bedrooms = fields.Integer(required=True)
    living_area = fields.Integer(copy=False)
    facades = fields.Integer(required=True)
    garage = fields.Boolean(required=True)
    garden = fields.Boolean(required=True)
    garden_area = fields.Integer(required=True)
    garage_orientation = fields.Selection(
        string='Type',
        selection=[('east', 'East'), ('west', 'West'),('north','North'),('south','South')],
        help="Type is used to separate Leads and Opportunities")


    
