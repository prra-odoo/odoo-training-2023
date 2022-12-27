# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime, timedelta

class estateModel(models.Model):
    _name = "estate.property"
    _description = "Real Estate Module"

    name = fields.Char('Name',required=True)
    description = fields.Text('Description',copy=False,required=True)
    postcode = fields.Char('Post Code',required=True)
    date_availability = fields.Date('Last Availability',default=lambda self:fields.Datetime.today())
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',copy=False,required=True)
    bedrooms = fields.Integer('Bedrooms',required=True)
    living_area = fields.Integer('Living Area',copy=False)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('done','Done')],default='new')
    garage_orientation = fields.Selection(
        string='Garden Orientation:',
        selection=[('east', 'East'), ('west', 'West'),('north','North'),('south','South')],
        help="Type is used to separate Leads and Opportunities")
    propertyid=fields.Many2one("estate.property.type", string="Property")


    
