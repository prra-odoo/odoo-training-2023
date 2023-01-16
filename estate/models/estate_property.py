# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

three_months = date.today() + relativedelta(months=+3)


class estate_property(models.Model):
    _name = "estate.property"
    _description = "estate property model"

    name = fields.Char(string = "Name", required = True, help = "this is name")
    description = fields.Text(string = "Description")
    postcode = fields.Char(string = "Pin Code", required = True)
    date_availability = fields.Date(string = "Availablity Date",copy = False,default = three_months)
    expected_price = fields.Float(string = "Expected Price", required = True)
    selling_price = fields.Float(string = "Selling Price",readonly = True,copy = False)
    bedrooms = fields.Integer(string = "Bedroom Number",default="2")
    living_area = fields.Integer(string = "Living Area")
    facades = fields.Integer(string = "Facades")
    garage = fields.Boolean(string = "Garage")
    garden = fields.Boolean(string = "Garden")
    garden_area = fields.Integer(string = "Garden Area")
    garden_orientation = fields.Selection(
        string = "Garden Orientation",
        selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(string = "Active")
    state = fields.Selection(
        string = "State",
        selection = [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new')
    property_type_id= fields.Many2one("estate.property.type",string="Property Type")
