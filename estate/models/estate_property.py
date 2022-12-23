# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta


class estatePropertyModel(models.Model):
    _name = "estate.property"
    _description = "Esate property model"

    name = fields.Char('Name:',required=True)
    postcode = fields.Char()
    description = fields.Text()
    date_availability = fields.Date(
        'Date availability', default=lambda self: fields.datetime.now() + relativedelta(months=6))
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living area' ,copy=False)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
    )
    active= fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('new','New'),('development','Development'),('done','Done')],
        default='new',
    )
