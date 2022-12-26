# -*- coding: utf-8 -*-

from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateModel(models.Model):
    _name = "estate.property"
    _description = "Estate Model"

    name = fields.Char('Name',required = True)
    description = fields.Text()
    note = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date('Date availability', readonly = True, default=lambda self: fields.datetime.now()+ relativedelta(months=3) )
    expected_price = fields.Float('Expected price', required = True)
    selling_price = fields.Float('Selling price', copy = False)
    bedrooms = fields.Integer()
    living_area = fields.Integer('Living area')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('Garden area')
    garden_orientation = fields.Selection(
            string='Garden orientation type',
            selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
        )
    active = fields.Boolean(default=True)
    state = fields.Selection(
            selection=[('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default="new"
        )
