# -*- coding: utf-8 -*-

from odoo import models,fields
from dateutil.relativedelta import relativedelta

class estateProperty(models.Model):
    _name = "estate.property"
    
    _description = "This is the description of the  estate property"

    name = fields.Char(required=True)
    id = fields.Integer()
    postcode = fields.Char()
    description = fields.Text(copy=False)
    date_availability = fields.Date('Date avilability',default=lambda self: fields.datetime.today()+relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True,default=2000000)
    bedrooms = fields.Integer(default=3)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    other_info=fields.Text()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    state = fields.Selection(selection = [('new', 'New'),
           ('in_progress', 'In Progress'),('cancel', 'Cancelled'),('done', 'Done')])

