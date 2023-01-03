# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

class Real_estate(models.Model):
    _name="estate.property.model" # according to the naming conventions we do not add model in model's name
    _description="Real Estate Model"

    name = fields.Char(required=True,default="New User")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=fields.date.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float("200",readonly=True,copy=False)
    bedrooms = fields.Integer(default="2")
    active = fields.Boolean(default=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    state=fields.Selection(
        string='State',
        selection=[('new','New'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancled','Canceled')],
        required=True,
        copy=False,
        default='new'
    )
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='orientation',
    selection=[('north','North'),('east','East'),('west','West'),('south','South')])

