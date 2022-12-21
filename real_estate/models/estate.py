# -- coding: utf-8 --

from odoo import fields, models

class realEstate(models.Model):
    _name = "estate.model"
    _description = "Estate model"

    name = fields.Char('name', required = True)
    description = fields.Text()
    postcode = fields.Char('Postcode', required=True)
    date_availability = fields.Date(default=lambda self: fields.Datetime.now())
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east','East'), ('west','West')],
        help="Type is used to separate Leads and Opportunities")