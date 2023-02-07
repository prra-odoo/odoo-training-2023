# -- coding: utf-8 --
from odoo import models, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate_property Model"
    
    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self:datetime.now()
                                    +relativedelta(months=+3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area= fields.Integer()
    facades = fields.Integer() 
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Garden Orientattion',
        selection = [('north','North'),('south','South'),
                     ('east','East'),('west','West')],
    )

    state = fields.Selection(
        selection = [('new','New'),('offer_received','Offer_Received'),
                     ('offer_accepted','Offer_Accepted'),('sold','Sold'),
                     ('cancelled','Cancelled')],
        string = 'Status',required=True,copy=False,default='new'
    ) 

    active = fields.Boolean(default=False)
